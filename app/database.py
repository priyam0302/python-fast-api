import json
from app.settings import DATABASE_FILE

def store_data(data):
    with open(DATABASE_FILE, "w") as f:
        json.dump(data, f, indent=4)
