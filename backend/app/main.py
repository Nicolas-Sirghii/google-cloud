from fastapi import FastAPI
from .database import get_message

app = FastAPI()

@app.get("/api/message")
def read_message():
    try:
        message = get_message()
        return {"message": message}
    except Exception as e:
        return {"message": f"Error: {str(e)}"}
