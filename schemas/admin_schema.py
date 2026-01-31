from pydantic import BaseModel, EmailStr
from typing import Optional

class AdminCreate(BaseModel):
    admin_id:Optional[str]=None
    name : str
    email : EmailStr
    phno : str
    password: str