from pydantic import BaseModel
from typing import Optional,Any,List


class BaseResponse(BaseModel):
    message:Optional[str] = None
    status_code:Optional[int] = None
    error:Optional[str] = None
    data:Optional[List[Any]] = None


class Team(BaseModel):
    team_id:Optional[int]
    team_name:Optional[str]



class Player(BaseModel):
    player_id:Optional[int]
    player_name:Optional[str]
    team:Optional[Team]

