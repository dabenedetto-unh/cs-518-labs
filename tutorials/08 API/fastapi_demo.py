from uuid import uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = {}

class Item(BaseModel):
    id: str = None
    name: str
    price: float
    description: str = None

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/")
def read_items():
    return items

@app.get("/items/{item_id}")
def read_item(item_id: str, q: str = None):
    print("item_id:", item_id)
    print("query:",q)
    i = items.get(item_id)
    if not i:
        raise HTTPException(status_code=404, detail="Item not found")
    return i

@app.post("/items/")
def create_item(item: Item):

    # add id to item
    item.id = str(uuid4())

    # add item to items
    items[item.id] = item

    return item

@app.put("/items/{item_id}")
def update_item(item_id: str, item: Item):
    return {"item_id": item_id, "item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"deleted": item_id}

# start the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("fastapi_demo:app", host="0.0.0.0", port=8000, reload=True)