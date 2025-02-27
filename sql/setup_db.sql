-- Create database
CREATE DATABASE amazon_sales;

-- Connect to the newly created database
\c amazon_sales;

-- Create table for storing Amazon sales data
CREATE TABLE amazon_sales_data (
    product_id VARCHAR(50) PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    discounted_price NUMERIC(10,2),
    actual_price NUMERIC(10,2),
    discount_percentage VARCHAR(10),
    rating NUMERIC(3,1),
    rating_count INT,
    review_title TEXT,
    review_content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
