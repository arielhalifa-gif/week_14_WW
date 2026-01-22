from fastapi import FastAPI, File, UploadFile
import pandas as pd
from models import DataManipulation as dm
from db import DbConnector as dc
import uvicorn

app = FastAPI()

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    file.file.close()
    df_new_column = dm.add_new_column(df)
    df_clean = dm.replace_null(df_new_column)
    # insert_message = dc.insert_data(df_clean)
    return {"status": 'insert_message',
            "inserted records": len(df_clean)}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port="8000")