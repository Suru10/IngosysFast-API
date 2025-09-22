from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Path Parameter Example")   

@app.get("/search/")
def search_events(topic: str, city: str = "New York"):
    return {"topic": topic, "city": city}   
