from models import *
from schema import *
from sqlalchemy.orm import Session
from exceptions import UserNotFoundException , UserIsAlreadyExistException , IsNotCorrectException
import psycopg2
from settings import DATABASE_URL

import bcrypt

def get_current_weight(* , username:str , db:Session):
    user = db.query(Weight).filter_by(username = username).all()
    
    
    if not user:
        raise UserNotFoundException()
    
    ls = []
    for i in user:
        ls.append(i.date)

    max_date = max(ls)

    for i in user:
        if i.date == max_date:
            result = user[user.index(i)].weight

    return {"weight" : result}



def create_user_in_db(* , data: UserCreateSchema , db:Session):
    hashed_password = bcrypt.hashpw(data.password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(username=data.username, password=hashed_password.decode('utf-8'), height = data.height)
    user = db.query(User).filter_by(username = data.username).first()

    if user:
        raise UserIsAlreadyExistException()
    

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg" : "user is created"}



def add_weight_profile(* , data: UserCreateWeightSchema , db:Session):
    user = db.query(User).filter_by(username = data.username).first()
    user_weight = db.query(Weight).filter_by(username = data.username , date = data.date).first()
    new_weight_for_user = Weight(username = data.username , weight = data.weight , date = data.date)

    if not user:
        raise UserNotFoundException()
    
    if user_weight:
        db.query(Weight).filter_by(username  = data.username , date = data.date).update({"weight": data.weight})
        db.commit()
        return{"msg" : "weight is added"}


    db.add(new_weight_for_user)
    db.commit()
    db.refresh(new_weight_for_user)

    return{"msg" : "weight is added"}


def get_differences_between_dates(* , username:str , db:Session):
    user = db.query(Weight).filter_by(username = username).all()
    if not user:
        raise UserNotFoundException()



    ls = []
    for i in user:
        ls.append(i.date)

    max_date = max(ls)
    min_date = min(ls)

    for i in user:
        if i.date == max_date:
            last_weight = user[user.index(i)].weight

        if i.date == min_date:
            first_weight = user[user.index(i)].weight


    if last_weight > first_weight:
        change = last_weight - first_weight
        return {"your weight change(weight gain)": change}
        
    elif first_weight > last_weight:
        change = first_weight - last_weight
        return {"your weight change(weight lose)" : change}
        
    else:
        return ("your weight has not changed")
    


def calculate_bmi_for_user(* , username:str , db:Session):
    user = db.query(User).filter_by(username = username).first()
    user_weight = db.query(Weight).filter_by(username = username).all()
    if not user_weight:
        raise UserNotFoundException

    ls = []
    for i in user_weight:
        ls.append(i.date)

    max_date = max(ls)

    for i in user_weight:
        if i.date == max_date:
            last_weight = user_weight[user_weight.index(i)].weight

    your_BMI_point = (last_weight/(user.height**2))*10000

    return {"your BMI point is " : round(your_BMI_point , 2)}


