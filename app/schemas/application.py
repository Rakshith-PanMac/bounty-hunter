from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime
from app.models.application import AppStatus

class ApplicationBase(BaseModel):
    company_name: str
    role_title: str
    job_url: Optional[HttpUrl] = None
    status: AppStatus = AppStatus.WISHLIST
    salary_range: Optional[str] = None
    follow_up_date: Optional[datetime] = None
    contact_person: Optional[str] = None
    material_used: Optional[str] = None
    notes: Optional[str] = None

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationRead(ApplicationBase):
    id: int
    date_applied: datetime
    evidence_path: Optional[str] = None
    match_score: Optional[int] = None

    class Config:
        from_attributes = True
