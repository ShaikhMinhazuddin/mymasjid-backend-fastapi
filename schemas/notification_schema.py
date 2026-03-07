from pydantic import BaseModel
from typing import Optional

def NotificationCreate(BaseModel):
    notificationId : str
    mosqueId : str
    subject : str
    type : str
    details : str
    additionalLinks : Optional[str]