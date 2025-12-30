from base_response import CreatePlayer,BaseResponse


def create_players(player:CreatePlayer):
    """vali"""

    data = player.model_dump(exclude_unset=False)
    print(data)

    return BaseResponse(message="exito",status_code=201,data=[data])