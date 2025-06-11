# Product Scraper (Local Mock Site)

This project is a simple Python script that uses Selenium to scrape product information from a local HTML file that simulates an e-commerce website. It demonstrates how to extract data from a JavaScript-rendered page and save it into a CSV file.

## What It Does

- Opens a local HTML page that loads products with JavaScript
- Uses Selenium in headless mode to read the rendered content
- Extracts product title, price, shipping, and link
- Saves the data into a CSV file

## Files

- scraper.py: the Python script that performs the scraping
- mock_store/mock_store.html: the mock e-commerce page
- products.csv: the output file with scraped data

## How to Run

1. Install the required libraries:

   pip install selenium webdriver-manager

2. Make sure mock_store.html is in the correct folder.

3. Run the scraper:

   python scraper.py

4. Open products.csv to view the results.

## Why This Is Useful

This project shows how to work with JavaScript-based pages using Selenium and how to structure and export scraped data. It is a safe and ethical way to demonstrate scraping skills without relying on live websites.
