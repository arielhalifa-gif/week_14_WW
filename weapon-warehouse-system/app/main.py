from fastapi import FastAPI, File, UploadFile
import pandas as pd
from models import DataManipulation as dm

app = FastAPI()

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    file.file.close()
    df_new_column = dm.add_new_column(df)
    df_clean = dm.replace_null(df_new_column)