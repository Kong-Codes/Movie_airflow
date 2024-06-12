FROM quay.io/astronomer/astro-runtime:11.4.0
FROM astronomerinc/ap-airflow:2.2.0-1-buster-onbuild
WORKDIR /usr/local/airflow
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["webserver", "timeout:120s"]