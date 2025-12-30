from pydantic import BaseModel
from typing import Optional,Any,List


class BaseResponse(BaseModel):
    message:Optional[str] = None
    status_code:Optional[int] = None
    error:Optional[str] = None
    data:Optional[List[Any]] = None


class Team(BaseModel):
    id_team:Optional[int]
    team_name:Optional[str]





