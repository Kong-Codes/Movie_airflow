Overview
========

The purpose of this Airflow project is to automate the process of updating information for 1000 movies per day. This process involves fetching the latest data for each movie, processing the data, and updating the respective records in a database. The automated workflow ensures data accuracy and consistency while saving time and reducing manual intervention.

Project Contents
================

- Data source: Omdb api and tmdb api.
- Data storage: Amazon s3 bucket
- Data processing: Snowflake


![Airflow diagram](include/static/airflow%20diagram.png)

## Technologies used
- Bash
- AWS
- Python  <br>
  *Dependencies used:*
  - apache-airflow
  - requests
  - pandas
  - python-dotenv
  - pytest


## Project build & setup 
___
- **setup development environment:** 
  - `poetry env use python3.9` 
  - `poetry install` 
<br>

- **Create dedicated database(S3 bucket)**

  - login to AWS as root user create IAM user account and get your access keys

  - create new bucket

  - grant user privileges on new IAM user for all amazon S3 bucket features

<br>

- **Create and define required airflow variables in the `airlow_setting.yaml` file**

        variables:
            - variable_name: apikey
              variable_value: <'api_key'>
            - variable_name: apitoken
              variable_value: <'api_token'>
            - variable_name: aws_access_key_id
              variable_value: <'IAM access key'>
            - variable_name: aws_secret_access_key
              variable_value: <'IAM secret key'>

- **run `astro dev start` to kickstart the building of the docker container and starting up the airflow  



Deploy Your Project Locally
===========================

I used Astro to deploy my airflow locally to enable testing before deployment to a cloud service such as (EC2) 


