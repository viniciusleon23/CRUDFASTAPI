from pydantic import BaseModel
from typing import Optional,Any,List
class BaseResponse(BaseModel):
    message:Optional[str]
    status_code:Optional[int]
    error:Optional[str]
    data:Optional[List[Any]]
