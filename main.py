from fastapi import FastAPI

#endpoints
from endpoints.healt_check import health_check

app = FastAPI()

@app.get("/api/v1/")
def healt():
    return  health_check()