from sqlalchemy.orm import Session
from sqlalchemy import update, or_, and_, func
from db.models import Invoice

def get_invoices_by_category(db: Session, category: str):
    return db.query(Invoice).filter(Invoice.category == category).all()

def mark_removal_order_ids(db: Session):
    db.execute(
        update(Invoice).
        where(func.length(Invoice.order_id) == 10).
        values(category='Removal Order IDs')
    )
    db.commit()

def mark_return(db: Session):
    db.execute(
        update(Invoice).
        where(and_(
            Invoice.transaction_type == 'Return',
            Invoice.invoice_amount.isnot(None),
            Invoice.invoice_amount != ''
        )).
        values(category='Return')
    )
    db.commit()

def mark_negative_payout(db: Session):
    db.execute(
        update(Invoice).
        where(and_(
            Invoice.transaction_type == 'Payment',
            Invoice.total < 0
        )).
        values(category='Negative Payout')
    )
    db.commit()

def mark_order_payment_received(db: Session):
    db.execute(
        update(Invoice).
        where(and_(
            Invoice.order_id.isnot(None),
            Invoice.total.isnot(None),
            Invoice.invoice_amount.isnot(None)
        )).
        values(category='Order & Payment Received')
    )
    db.commit()

def mark_order_not_applicable_payment_received(db: Session):
    db.execute(
        update(Invoice).
        where(and_(
            Invoice.order_id.isnot(None),
            Invoice.total.isnot(None),
            or_(Invoice.invoice_amount.is_(None), Invoice.invoice_amount == '')
        )).
        values(category='Order Not Applicable but Payment Received')
    )
    db.commit()

def mark_payment_pending(db: Session):
    db.execute(
        update(Invoice).
        where(and_(
            Invoice.order_id.isnot(None),
            Invoice.invoice_amount.isnot(None),
            or_(Invoice.total.is_(None), Invoice.total == '')
        )).
        values(category='Payment Pending')
    )
    db.commit()