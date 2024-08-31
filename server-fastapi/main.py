from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from dotenv import load_dotenv
import os
from api.upload import router as upload_router

from db import crud, models
from db.database import SessionLocal, engine

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

frontend_url = os.getenv("FRONTEND_URL")
####
# Cors rules
origins = [frontend_url]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
####

#### Dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
####


# app router
app.include_router(upload_router, prefix="/api")

@app.get("/")
async def root(db: Session = Depends(get_db)):
    data = os.getenv("FRONTEND_URL")
    return {"message": "Hello World db url king {}".format(data)}