from fastapi import FastAPI, Form, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from chain import get_responsef
from ingest import ingest_pdf_file
import shutil
import os
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
def chat(user_input: str = Form(...)):
    response = get_responsef(user_input)
    return {"response": response}

@app.post("/ingest-pdf")
async def ingest_pdf(file: UploadFile = File(...)):
    # Save the uploaded file to a temporary location
    temp_dir = "../data/uploaded_pdfs"
    os.makedirs(temp_dir, exist_ok=True)
    temp_file_path = os.path.join(temp_dir, f"{uuid.uuid4()}_{file.filename}")
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    try:
        ingest_pdf_file(temp_file_path)
        return {"status": "success", "message": "PDF ingested successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        os.remove(temp_file_path)