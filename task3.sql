-- SQL Script: Sales Data Analysis for Online Store

-- 1. Calculate the total sales volume for March 2024
SELECT 
    SUM(amount) AS total_sales_march_2024
FROM 
    orders
WHERE 
    strftime('%Y-%m', order_date) = '2024-03';
-- Expected Result: 27,000


-- 2. Find the customer who spent the most overall
SELECT 
    customer, 
    SUM(amount) AS total_spent
FROM 
    orders
GROUP BY 
    customer
ORDER BY 
    total_spent DESC
LIMIT 1;
-- Expected Result: Alice (20,000)


-- 3. Calculate the average order value for the last three months (Jan–Mar 2024)
SELECT 
    ROUND(SUM(amount) * 1.0 / COUNT(*), 2) AS average_order_value
FROM 
    orders
WHERE 
    order_date BETWEEN '2024-01-01' AND '2024-03-31';
-- Expected Result: 6,000 (48,000 total sales / 8 orders)
