from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message1": "Welcome to the DevOps world",
        "message2": "Happy to learn coding",
        "message3": "Excellent decision"
    }