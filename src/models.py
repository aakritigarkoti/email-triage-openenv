from pydantic import BaseModel
from typing import List, Optional

class Email(BaseModel):
    id: str
    subject: str
    body: str
    sender: str
    true_label: str  # spam / normal / urgent

class Action(BaseModel):
    type: str  # classify / reply / ignore
    email_id: str
    label: Optional[str] = None

class Observation(BaseModel):
    emails: List[Email]