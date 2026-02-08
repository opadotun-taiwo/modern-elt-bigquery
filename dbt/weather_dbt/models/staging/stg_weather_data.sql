{{
    config(
        materialized='incremental',
        unique_key='weather_id'
    )
}}

with source as (
    select *
    from {{source('weather_data', 'raw_weather_data')}}
),

de_dup as (
    select *,
        row_number() over(partition by time order by inserted_at) as rn
    from source
)

select
    {{ dbt_utils.generate_surrogate_key([
            'city',
            'time'
        ]) }} as weather_id,
    city,
    temperature,
    weather_descriptions,
    wind_speed,
    time as weather_time_local,
    timestamp_add(
    inserted_at,
    interval CAST(ROUND(CAST(utc_offset AS FLOAT64)) AS INT64) hour
    ) as inserted_at_local

from de_dup
where rn = 1

