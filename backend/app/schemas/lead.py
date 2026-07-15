from pydantic import BaseModel, EmailStr


class LeadCreate(BaseModel):
    name: str
    phone: str
    email: EmailStr
    city: str
    event_type: str
    budget: str
    source: str


class LeadResponse(LeadCreate):
    id: str
    status: str

    model_config = {
        "from_attributes": True
    }