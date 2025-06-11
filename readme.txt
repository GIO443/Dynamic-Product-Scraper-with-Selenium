# Simulated E-Commerce Product Scraper

This project demonstrates a Python-based Selenium scraper that extracts product data from a locally hosted, JavaScript-rendered mock e-commerce page. It showcases the ability to work with dynamic content, structured extraction, and clean CSV output — all while avoiding ethical or legal concerns related to scraping live commercial websites.

## What It Does

- Launches a headless browser using Selenium
- Loads a local HTML file that simulates a product listing page
- Waits for JavaScript to render products
- Extracts product title, price, shipping info, and URL
- Saves the results to a clean `products.csv` file

## Technologies Used

- Python 3
- Selenium
- ChromeDriver (via `webdriver-manager`)
- HTML + JavaScript (for the mock store)
- CSV for data output

## Project Structure

selenium-scraper/
├── mock_store/
│ └── mock_store.html # Simulated dynamic store (JS-rendered)
├── scraper.py # Selenium script
├── products.csv # Scraped output
└── README.md # Project documentation

## Sample Output

| Title                 | Price  | Shipping       | Link              |
|----------------------|--------|----------------|-------------------|
| Gaming Laptop Pro    | $1299  | Free Shipping  | product1.html     |
| Ultrabook X15        | $899   | $15 Shipping   | product2.html     |
| Budget Laptop Z      | $499   | Free Shipping  | product3.html     |

## How to Run

1. Install dependencies:

In bash
pip install selenium webdriver-manager

2. Run the scraper:

python scraper.py