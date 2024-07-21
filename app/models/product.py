from pydantic import BaseModel

class Product(BaseModel):
    title: str
    price: float
    image_url: str
