from fastapi import FastAPI, Depends
from db import get_db
from sqlalchemy.orm import session
from schema import *
from service import *
app = FastAPI()


@app.get("/")
def health_check():
    return { "msg": "health check is passed"}


@app.get("/weight")
def current_weight(username:str , db:Session = Depends(get_db)):
    message = get_current_weight(username = username , db = db)
    return message

@app.post("/weight")
def create_weight(item: UserCreateWeightSchema , db: Session = Depends(get_db)):
    message = add_weight_profile(data = item , db = db)
    return message
    

@app.get("/weight/difference")
def differences_weight(username:str,  db:Session = Depends(get_db)):
    message = get_differences_between_dates(username=username , db = db)
    return message

@app.get("/weight/bmi")
def calculate_bmi(username:str , db:Session = Depends(get_db)):
    message = calculate_bmi_for_user(username=username , db= db)
    return message



@app.post("/user")
def create_user(item: UserCreateSchema , db:Session = Depends(get_db)):
    message = create_user_in_db(data = item , db = db)
    return message