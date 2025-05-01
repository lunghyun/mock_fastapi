from fastapi import FastAPI

app = FastAPI()

@app.get("/ai/hello")
def hello():
    return {"message": "Hello from FastAPI mock!"}
