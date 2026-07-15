from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.lead import LeadCreate, LeadResponse
from app.crud.lead import (
    create_lead,
    get_leads,
    get_lead,
    update_lead,
    delete_lead,
)
from app.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/leads",
    tags=["Leads"]
)


@router.post(
    "/",
    response_model=LeadResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_lead(
    lead: LeadCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return create_lead(db, lead)


@router.get(
    "/",
    response_model=list[LeadResponse]
)
def read_leads(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return get_leads(db)


@router.get(
    "/{lead_id}",
    response_model=LeadResponse
)
def read_lead(
    lead_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    lead = get_lead(db, lead_id)

    if not lead:
        raise HTTPException(
            status_code=404,
            detail="Lead not found"
        )

    return lead


@router.put(
    "/{lead_id}",
    response_model=LeadResponse
)
def update_existing_lead(
    lead_id: UUID,
    lead: LeadCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    updated = update_lead(db, lead_id, lead)

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Lead not found"
        )

    return updated


@router.delete("/{lead_id}")
def remove_lead(
    lead_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    deleted = delete_lead(db, lead_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Lead not found"
        )

    return {
        "message": "Lead deleted successfully"
    }