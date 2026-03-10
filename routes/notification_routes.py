from fastapi import APIRouter, HTTPException
from database import supabase

router = APIRouter(prefix="/notifications")

@router.get("/{mosque_id}")
def get_notification(mosque_id : str):
    try:
        results  = supabase.table("notifications").select("*").eq("mosque_id",mosque_id).execute()
        return results.data
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
