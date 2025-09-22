from fastapi import FastAPI
import uvicorn
from fastapi.responses import HTMLResponse

app = FastAPI(title="AI Assistant")

@app.get("/", response_class=HTMLResponse)
def homepage():
    return """
    <html>
        <head>
            <title>AI Assistant</title>
        </head>
        <body>
            <h1>Welcome to the AI Assistant</h1>
            <p>This is a simple FastAPI application.</p>
        </body>
    </html>
    """
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)