import unittest
from app.scraper import scrape_products

class TestScraper(unittest.TestCase):
    def test_scrape_products(self):
        products = scrape_products(1, None)
        self.assertGreater(len(products), 0)
        for product in products:
            self.assertIsInstance(product, Product)

if __name__ == "__main__":
    unittest.main()
