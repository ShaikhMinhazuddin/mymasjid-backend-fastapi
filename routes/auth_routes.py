from fastapi import APIRouter, HTTPException
from schemas.mosque_schema import MosqueRegistration
from database import supabase
from services.auth_service import register_mosque
from auth.password import verify_password

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register-mosque")
def register_mosque_api(data: MosqueRegistration):
    return register_mosque(data)

@router.post("/login")
def login(email:str, password:str):
    result = supabase.table("admin").select("*").eq("email",email).execute()
    
    if not result.data:
        raise HTTPException(status_code=401, detail ="Invalid Credentials")
    
    admin = result.data
    
    if not verify_password(password, admin["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    return {
        "message":"Login Successful",
        "admin_id":admin["id"],
        "mosque_id":admin["mosque_id"]
    }