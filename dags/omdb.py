import requests
import boto3
import pandas as pd
import pyarrow
import pandas as pd
from io import StringIO
from dotenv import load_dotenv
from airflow.models import Variable

load_dotenv()

s3_client = boto3.client(
    's3',
    aws_access_key_id=Variable.get('aws_access_key_id'),
    aws_secret_access_key=Variable.get('aws_secret_access_key')
)


def update_airflow_values(ti):
    start = ti.xcom_pull(key='start', task_ids='initialize')
    end = ti.xcom_pull(key='end', task_ids='initialize')
    print(f"Current Start: {start}, Current End: {end}")
    start += 100
    end += 100
    print(f"Updated Start: {start}, Updated End: {end}")
    ti.xcom_push(key='start', value=start)
    ti.xcom_push(key='end', value=end)


def extract(ti):
    start = ti.xcom_pull(key='start', task_ids='initialize')
    end = ti.xcom_pull(key='end', task_ids='initialize')
    api_token = Variable.get("apitoken")
    api = Variable.get("apikey")
    api_data = pd.DataFrame(columns=["Title", "Year", "Rated", "Runtime", "Genre",
                                     "Director", "Actors", "Plot", "Language", "Country", "Poster", "imdbRating",
                                     "Type"])
    obj = s3_client.get_object(Bucket='omdb-bucket', Key='movie.csv')
    df = pd.read_csv(StringIO(obj['Body'].read().decode('utf-8')))

    df.to_csv('main.csv')
    for num in range(start, end):
        url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={num}&sort_by=popularity.desc"

        headers = {
            "accept": "application/json",
            "Authorization": api_token
        }

        response = requests.get(url, headers=headers)

        for num_ in range(20):
            title = response.json()['results'][num_]["original_title"]
            url = f"https://www.omdbapi.com/?t={title}&apikey={api}"

            response_ = requests.get(url)

            if response_.json()['Response'] == "True":
                data_movie = pd.DataFrame({"Title": [response_.json()['Title']], 'Year': [response_.json()['Year']],
                                           'Rated': [response_.json()['Rated']],
                                           'Runtime': [response_.json()['Runtime']],
                                           'Genre': [response_.json()['Genre']],
                                           'Director': [response_.json()['Director']],
                                           'Actors': [response_.json()['Actors']],
                                           'Plot': [response_.json()['Plot']],
                                           'Language': [response_.json()['Language']],
                                           'Country': [response_.json()['Country']],
                                           'Poster': [response_.json()['Poster']],
                                           'imdbRating': [response_.json()['imdbRating']],
                                           'Type': [response_.json()['Type']]})

                data_movie.to_csv('main.csv', mode='a', header=False, index=False)

    s3_client.upload_file('main.csv', 'omdb-bucket', 'movie.csv')
