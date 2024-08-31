import pandas as pd
from io import StringIO
from sqlalchemy import delete
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import Invoice
import math
from datetime import datetime

def save_to_db(file):

    df = file.data

    # save data to postgresql

    df.columns = [col.replace(' ', '_').lower() for col in df.columns]

    # print(df["invoice_date"])

    def parseNone(value):
        if value is None or (isinstance(value, str) and value.lower() == 'nan') or (isinstance(value, float) and math.isnan(value)):
            return None
        else:
            return value

    def checkValidDate(value, date_format='%m/%d/%y'):
        if value:
            try:
                return datetime.strptime(value, date_format)
            except ValueError:
            # Handle the case where the date string does not match the format
                return None
        else:
            return None
        
    # # # # Convert DataFrame to a list of Invoice objects
    invoices = []
    for _, row in df.iterrows():
        invoice = Invoice(
            date_time=checkValidDate(row.get('date_time')),
            payment_type=parseNone(row.get('payment_type')),
            order_id=parseNone(row.get('order_id')),
            description=parseNone(row.get('description')),
            total=parseNone(row.get('total')),
            invoice_date=parseNone(row.get('invoice_date')),
            transaction_type=parseNone(row.get('transaction_type')),
            shipment_date=parseNone(row.get('shipment_date')),
            order_date=parseNone(row.get('order_date')),
            shipment_item_id=parseNone(row.get('shipment_item_id')),
            item_description=parseNone(row.get('item_description')),
            invoice_amount=parseNone(row.get('invoice_amount'))
        )
        invoices.append(invoice)

   
    clear_and_upload_invoices(invoices)
    
    return df

def clear_and_upload_invoices(invoices):
     # # # Insert the invoices into the database
    with SessionLocal() as session:
        # Delete all
        session.execute(delete(Invoice))
        session.commit()  # Commit the delete operatio

        session.bulk_save_objects(invoices)
        print("upload done\n")
        session.commit()
    
    return {}