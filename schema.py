from pydantic import BaseModel
from datetime import date


class UserCreateSchema(BaseModel):
    username:str
    password:str
    height:float

    class Config:
        extra = "forbid"


class WeightGetSchema(BaseModel):
    username:str
    
    class Config:
        extra = "forbid"



class UserCreateWeightSchema(BaseModel):
    username:str
    weight:float
    date:date
    class Config:
        extra = "forbid"


