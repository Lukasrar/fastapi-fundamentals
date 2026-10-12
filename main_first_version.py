from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "healthy"}


items = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]


@app.get("/items")
def get_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}


@app.post("/items")
def create_item(item: dict):
    new_id = max(item["id"] for item in items) + 1 if items else 1
    item["id"] = new_id
    items.append(item)
    return item