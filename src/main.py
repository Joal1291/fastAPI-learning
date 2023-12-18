from typing import Union, Optional

from fastapi import FastAPI, HTTPException
from fastapi import Path, Query
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

app = FastAPI()

inventory = {}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description ="The ID of the item you'd like to view")):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not in inventory")
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name : str = Query(None, description="The name of the item you are looking for")):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail="Item not found in the inventory")

@app.get("/all_item")
def get_all_item():
    return inventory

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=405, detail="Item allready exist")
    
    inventory[item_id] = item
    raise HTTPException(status_code=200, detail="Item created with succes")