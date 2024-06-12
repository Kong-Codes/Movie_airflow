Overview
========

The purpose of this Airflow project is to automate the process of updating information for 1000 movies per day. This process involves fetching the latest data for each movie, processing the data, and updating the respective records in a database. The automated workflow ensures data accuracy and consistency while saving time and reducing manual intervention.

Project Contents
================

- Data source: Omdb api and tmdb api.
- Data storage: Amazon s3 bucket
- Data transformation: Snowflake

Deploy Your Project Locally
===========================

I used Astro to deploy my airflow locally to enable testing before deployment to a cloud service such as (EC2) 


