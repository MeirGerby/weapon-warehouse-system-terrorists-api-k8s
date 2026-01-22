from typing import Annotated
import pandas as pd
from fastapi import FastAPI, File, UploadFile, HTTPException
import uvicorn
from db import insert_data

app = FastAPI()

def clean_data(file):
    df = pd.read_csv(file.file)
    bins = [-float("inf"), 20, 100, 300, float("inf")]
    labels = ["low", "medium", "high", "extreme"]
    df["risk_level"] = pd.cut(df["range_km"], bins=bins, labels=labels)
    df.fillna("Unknown", inplace=True)
    print(df)
    file.file.close()
    return df

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    df = clean_data(file) 
    print(df.columns)
    m = insert_data(df)
    if m:
        return {
            "status": "success",
            "inserted_records": 20
            } 
    else: 
        return {"status": "False"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
