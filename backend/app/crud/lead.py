from uuid import UUID
from sqlalchemy.orm import Session

from app.models.lead import Lead
from app.schemas.lead import LeadCreate


def create_lead(db: Session, lead: LeadCreate):
    """
    Create a new lead.
    """
    db_lead = Lead(
        name=lead.name,
        phone=lead.phone,
        email=lead.email,
        city=lead.city,
        event_type=lead.event_type,
        budget=lead.budget,
        source=lead.source,
    )

    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)

    return db_lead


def get_leads(db: Session):
    """
    Return all leads.
    """
    return db.query(Lead).all()


def get_lead(db: Session, lead_id: UUID):
    """
    Get a single lead by ID.
    """
    return db.query(Lead).filter(Lead.id == lead_id).first()


def update_lead(db: Session, lead_id: UUID, lead: LeadCreate):
    """
    Update an existing lead.
    """
    db_lead = get_lead(db, lead_id)

    if not db_lead:
        return None

    db_lead.name = lead.name
    db_lead.phone = lead.phone
    db_lead.email = lead.email
    db_lead.city = lead.city
    db_lead.event_type = lead.event_type
    db_lead.budget = lead.budget
    db_lead.source = lead.source

    db.commit()
    db.refresh(db_lead)

    return db_lead


def delete_lead(db: Session, lead_id: UUID):
    """
    Delete a lead.
    """
    db_lead = get_lead(db, lead_id)

    if not db_lead:
        return None

    db.delete(db_lead)
    db.commit()

    return db_lead