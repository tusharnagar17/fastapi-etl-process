from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from dotenv import load_dotenv
import os
from api.upload import router as upload_router

from db import crud, models
from db.database import SessionLocal, engine
from db.crud import get_invoices_by_category


# load all tables
models.Base.metadata.create_all(bind=engine)

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

# update invoice
def update_invoices(db):
    crud.mark_removal_order_ids(db)
    crud.mark_return(db)
    crud.mark_negative_payout(db)
    crud.mark_order_payment_received(db)
    crud.mark_order_not_applicable_payment_received(db)
    crud.mark_payment_pending(db)


# app router
app.include_router(upload_router, prefix="/api")

@app.get("/")
async def root(db: Session = Depends(get_db)):
    data = os.getenv("FRONTEND_URL")
    return {"message": "Hello World db url king {}".format(data)}

@app.get('/dashboard')
async def read_dashboard(db: Session = Depends(get_db)):
    # Invoke update invoice function
    update_invoices(db)

    # return data to frontend
    removal_order_ids = get_invoices_by_category(db, 'Removal Order IDs')
    returns = get_invoices_by_category(db, "Return")
    negative_payouts = get_invoices_by_category(db, "Negative Payout")
    order_payment_received = get_invoices_by_category(db, 'Order & Payment Received')
    order_not_applicable_payment_received = get_invoices_by_category(db, 'Order Not Applicable but Payment Received')
    payment_pending = get_invoices_by_category(db, 'Payment Pending')

    return {
        "removal_order_ids": removal_order_ids,
        "returns": returns,
        "negative_payouts": negative_payouts,
        "order_payment_received": order_payment_received,
        "order_not_applicable_payment_received": order_not_applicable_payment_received,
        "payment_pending": payment_pending
    }