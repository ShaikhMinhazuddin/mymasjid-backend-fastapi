from pydantic import BaseModel
from typing import Optional

def PrayerTimeCreate(BaseModel):
    masjidId : str
    fajr_adhan: str
    fajr_jamat: str
    zuhr_adhan: str
    zuhr_jamat: str
    asr_adhan: str
    asr_jamat: str
    magrib_adhan: str
    magrib_jamat: str
    isha_adhan: str
    isha_jamat: str