from fastapi import APIRouter, UploadFile, File
import os
import shutil

from app.services.resume_parser import extract_text_from_pdf

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    
    # Save file locally
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    extracted_text = extract_text_from_pdf(file_path)

    return {
        "filename": file.filename,
        "text": extracted_text[:1000]  # limit output for now
    }