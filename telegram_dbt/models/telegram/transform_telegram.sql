
  create view "telegram_data"."public"."transform_telegram__dbt_tmp"
    
    
  as (
    WITH cleaned_data AS (
    SELECT 
        message_id,
        channel,
        text AS message_text,
        date::TIMESTAMP AS message_date,
        media,
        image_path
    FROM public.telegram_data
    WHERE text IS NOT NULL
)

SELECT * FROM cleaned_data;
  );