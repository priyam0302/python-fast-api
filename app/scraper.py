import requests
from bs4 import BeautifulSoup
from app.models.product import Product
from app.settings import PROXY_URL, PAGES_LIMIT

def scrape_products(pages_limit, proxy):
    products = []
    for page in range(1, pages_limit + 1):
        url = f"https://example.com/products?page={page}"
        response = requests.get(url, proxies={"http": proxy, "https": proxy} if proxy else None)
        soup = BeautifulSoup(response.content, "html.parser")
        for product_element in soup.find_all("div", {"class": "product"}):
            title = product_element.find("h2", {"class": "title"}).text.strip()
            price = float(product_element.find("span", {"class": "price"}).text.strip().replace("$", ""))
            image_url = product_element.find("img", {"class": "image"})["src"]
            products.append(Product(title=title, price=price, image_url=image_url))
    return products
