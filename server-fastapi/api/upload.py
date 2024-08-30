from fastapi import APIRouter, File, UploadFile, Request, BackgroundTasks
from utils.myFunction import process_csv
from fastapi.responses import StreamingResponse
from io import BytesIO
import pandas as pd

router = APIRouter()

# update data to db
def load_data(df):
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
  
    # # Process the CSV files in the background
    # merged_df = process_csv(payment_report.file, merchant_report.file)

    # # Convert DataFrame to CSV
    # csv_buffer = BytesIO()
    # merged_df.to_csv(csv_buffer, index=False)
    # csv_buffer.seek(0)

    # return StreamingResponse(
    #     csv_buffer,
    #     media_type="text/csv",
    #     headers={"Content-Disposition": f"attachment; filename=merged_data.csv"}
    # )

    background_tasks.add_task(process_csv, payment_contents, merchant_contents)
    
    return {
        "payment_report_filename": payment_report.filename,
        "merchant_report_filename": merchant_report.filename,
        "message": "File upload in progress"
    }