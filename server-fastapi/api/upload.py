from fastapi import APIRouter, File, UploadFile, Request, BackgroundTasks
from utils.myFunction import process_csv
from fastapi.responses import StreamingResponse
from io import BytesIO
import pandas as pd

router = APIRouter()

# update data to db
def save_to_db(df):
    
    return {}

    
@router.get('/upload')
async def get_route():
    return {"message": "my message your are at /upload endpoint"}

@router.post("/upload")
async def upload_files(
    background_tasks: BackgroundTasks,
    payment_report: UploadFile = File(...),
    merchant_report: UploadFile = File(...),
):
    # Read the contents of the files
    payment_contents = await payment_report.read()
    merchant_contents = await merchant_report.read()

    background_tasks.add_task(process_csv, payment_contents, merchant_contents)
    
    return {
        "payment_report_filename": payment_report.filename,
        "merchant_report_filename": merchant_report.filename,
        "message": "File upload in progress"
    }