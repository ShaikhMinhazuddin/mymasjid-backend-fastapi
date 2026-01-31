from pydantic import BaseModel
from typing import Optional

from schemas.admin_schema import AdminCreate

class MosqueCreate(BaseModel):
    mosque_id: Optional[str] = None
    mosque_name : str
    address : str
    city : str
    state : str
    pin_code : str
    contact_number : str
    longitude : float
    latitude : float
    
class MosqueRegistration(BaseModel):
    admin: AdminCreate
    mosque : MosqueCreate