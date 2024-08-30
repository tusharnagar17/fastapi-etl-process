from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from api.upload import router as upload_router

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

frontend_url = os.getenv("FRONTEND_URL")
# Cors rules
origins = [frontend_url]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app router
app.include_router(upload_router, prefix="/api")

@app.get("/")
async def root():
    data = os.getenv("FRONTEND_URL")
    return {"message": "Hello World db url king {}".format(data)}