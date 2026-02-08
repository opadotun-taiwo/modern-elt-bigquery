{{
    config(
        materialized='table',
        unique_key='weather_id'
    )
}}

select 
    city,
    weather_descriptions,
    wind_speed,
    weather_time_local
from {{ ref('stg_weather_data') }}