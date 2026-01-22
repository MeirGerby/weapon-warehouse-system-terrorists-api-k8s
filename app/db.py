import os
import mysql.connector 
from pandas import DataFrame 
import pandas as pd 

MYSQL_ROOT_USER = os.getenv('MYSQL_ROOT_USER', default="root")
MYSQL_ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD', default="Meirgerby2001#")
MYSQL_ROOT_HOST = os.getenv('MYSQL_ROOT_HOST', default="localhost")
MYSQL_ROOT_DB = os.getenv('MYSQL_ROOT_DB', "weapons")

def get_connection():
    con = mysql.connector.connect(
    host=MYSQL_ROOT_HOST,
    user=MYSQL_ROOT_USER,
    password=MYSQL_ROOT_PASSWORD
    )
    if not con:
        raise ConnectionError("error: there is no connection")
    return con 

def create_table():
    db = get_connection()
    mycursor = db.cursor()
    try:
        mycursor.execute("CREATE DATABASE IF NOT EXISTS weapons")

        mycursor.execute(
            """CREATE TABLE IF NOT EXISTS weapons (
            id int NOT NULL ,
            weapon_id int NOT NULL,
            weapon_name varchar(255),
            weapon_type varchar(255),
            range_km int,
            weight_kg decimal,
            manufacturer varchar(255),
            origin_country varchar(255),
            storage_location varchar(255),
            year_estimated int,
            level_risk varchar(255),
            PRIMARY KEY (id)
            );"""
        )
        return True
    except:
        return False 
    
def insert_data(df: DataFrame):
    con = get_connection()
    mycursor = con.cursor()
    try:
        df.to_sql(con=con, name='weapons', if_exists='replace', method="multi") 
        return True 
    except:
        return False



