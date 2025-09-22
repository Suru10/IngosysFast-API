from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Exercise 1")   

@app.get("/welcome/{user_name}")
def welcome_user(user_name: str):
    return {f"Welcome {user_name} to Event Organizer Portal!", user_name}

@app.get("/event-count/")
def event_count(year: int):
    return {f"Number of events planned in {year}: 5", year}

