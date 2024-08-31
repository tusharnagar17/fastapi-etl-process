from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, Text, DECIMAL, Date
from sqlalchemy.orm import relationship

from .database import Base

class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True, index=True)
    date_time = Column(TIMESTAMP, nullable=True)
    payment_type = Column(String(50), nullable=True)
    order_id = Column(String(100), nullable=True)
    description = Column(Text, nullable=True)
    total = Column(DECIMAL(12, 2), nullable=True)
    invoice_date = Column(Text, nullable=True)
    transaction_type = Column(String(50), nullable=True)
    shipment_date = Column(Date, nullable=True)
    order_date = Column(Date, nullable=True)
    shipment_item_id = Column(String(100), nullable=True)
    item_description = Column(Text, nullable=True)
    invoice_amount = Column(DECIMAL(12, 2), nullable=True)