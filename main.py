from fastapi import FastAPI

#endpoints
from endpoints.healt_check import health_check
from endpoints.create_player import create_players

#respuestas
from base_response import CreatePlayer

app = FastAPI()

@app.get("/api/v1/")
def healt():
    return  health_check()


@app.post("/api/v1/player")
def player(player:CreatePlayer):
    return create_players(player)