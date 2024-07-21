Scraper Project
================

This project is a web scraper built using FastAPI and Python. It scrapes product data from a website and stores it in a JSON database.

Getting Started
---------------

1. Install the dependencies listed in `requirements.txt` using `pip install -r requirements.txt`.
2. Run the application using `uvicorn app.main:app --host 0.0.0.0 --port 8000`.
3. Send a POST request to `http://localhost:8000/scrape` with the required settings in the request body.

Settings
--------

* `pages_limit`: The number of pages to scrape.
* `proxy`: The proxy URL to use for scraping.

Database
---------

The scraped data is stored in a JSON file named `scraped_data.json`.

Tests
-----

Run the unit tests and integration tests using `pytest`.

License
-------

This project is licensed under the MIT License.
