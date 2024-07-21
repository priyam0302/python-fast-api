import unittest
from fastapi.testclient import TestClient
from app.main import app

class TestIntegration(unittest.TestCase):
    def test_scrape_endpoint(self):
        client = TestClient(app)
        response = client.post("/scrape", json={"pages_limit": 1, "proxy": None})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Scraping completed successfully")

if __name__ == "__main__":
    unittest.main()
