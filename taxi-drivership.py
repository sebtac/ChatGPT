

SELECT 
    EXTRACT(MONTH FROM pickup_datetime) AS month, 
    COUNT(*) AS rides, 
    CASE 
        WHEN passenger_count = 1 THEN 'Single Rider' 
        WHEN passenger_count > 1 THEN 'Multiple Riders' 
    END AS taxi_type 
FROM nyc_taxi 
GROUP BY month, taxi_type 
ORDER BY month, taxi_type;