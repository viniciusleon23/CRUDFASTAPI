from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1")
def healt_check():
    return {"message":"ok"}