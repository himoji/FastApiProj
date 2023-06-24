from fastapi import FastAPI, Path, Query, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: str | None

class UpdateItem(BaseModel):
    name: str | None
    price: float | None
    brand: str | None

inv = {}



@app.get("/")
def root():
    return {"data": "Hello World"}

@app.get("/home")
def home():
    return {"data": "home"}

@app.get("/get/{item_id}")
def get_item(item_id: int = Path(description="The ID of the item you need.", gt=0)):
    if item_id not in inv:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return inv[item_id]

@app.get("/get-by-name")
def get_item_by_name(name: str = Query(None, title="Name", description="Get item by its name")):
    for item_id in inv:
        if inv[item_id].name == name:
            return inv[item_id]

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inv:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Item ID is already exists (item already exists)\n use update-item to change its values!")

    inv[item_id] = item
    raise HTTPException(status_code=status.HTTP_201_CREATED)
    #return inv[item_id]


@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inv:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if item.name != None:
        inv[item_id].name = item.name

    if item.price != None:
        inv[item_id].price = item.price

    if item.brand != None:
        inv[item_id].brand = item.brand

    raise HTTPException(status_code=status.HTTP_200_OK)
    #return inv[item_id]