from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Path Parameter Example")

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

