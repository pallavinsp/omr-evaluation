from fastapi import FastAPI, UploadFile, File
import shutil, os
from omr_engine import pipeline

app = FastAPI()
UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def root():
    return {"message": "OMR API running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = pipeline.evaluate_sheet(file_path)
    return {"status": "success", "scores": result}
