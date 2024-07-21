from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from app.scraper import scrape_products
from app.database import store_data

app = FastAPI()

@app.post("/scrape")
async def scrape(request: Request):
    settings = await request.json()
    pages_limit = settings.get("pages_limit", 10)
    proxy = settings.get("proxy", None)
    data = scrape_products(pages_limit, proxy)
    store_data(data)
    return JSONResponse(content={"message": "Scraping completed successfully"}, status_code=200)
