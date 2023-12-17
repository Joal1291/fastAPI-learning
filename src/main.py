from typing import Union

from fastapi import FastAPI, Path, HTTPException, Query

app = FastAPI()

inventory = {
    1: {
        "name":"milk",
        "price": 132,
        "brand": "regular"
    },
    2: {
        "name":"playstation",
        "price": 132,
        "brand": "regular"
    },
    3: {
        "name":"fromage",
        "price": 132,
        "brand": "regular"
    },
    4: {
        "name":"xbox",
        "price": 132,
        "brand": "regular"
    }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description ="The ID of the item you'd like to view")):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not in inventory")
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name : str = Query(None, description="The name of the item you are looking for")):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail="Item not found in the inventory")

@app.get("/all_item")
def get_all_item():
    return inventory