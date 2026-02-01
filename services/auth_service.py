import uuid
from database import supabase
from auth.password import hash_password
from utils.id_generator import generate_mosque_id

def register_mosque(data):
    mosque_id = generate_mosque_id(
        data.mosque.mosque_name,
        data.mosque.pin_code
    )
    
    mosque_data = data.mosque.dict()
    mosque_data["mosque_id"] = mosque_id
    supabase.table("mosques").insert(mosque_data).execute()
    
    supabase.table("admins").insert({
        "admin_id": str(uuid.uuid4()),
        "name" : data.admin.name,
        "email": data.admin.email,
        "phno":data.admin.phno,
        "password" : hash_password(data.admin.password),
        "mosque_id" : mosque_id
        }).execute()
    
    return {
        "message" : "Mosque registered successfully",
        "mosque_id" : mosque_id
    }