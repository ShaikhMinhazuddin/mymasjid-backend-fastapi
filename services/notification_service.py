import uuid
from database import supabase

def createNotification(data):
    notificationId = str(uuid.uuid4())
    supabase.table("notifications").insert({
        "notification_id" : notificationId,
        "mosque_id" : data.mosqueId,
        "subject" : data.subject,
        "notification_type" : data.type,
        "details" : data.details,
        "additional_links" : data.additionalLinks
    }).execute()
    
    return {
        "message" : "Notification Created Successfully"
    }
    
def getNotificationByMosque(mosqueId : str):
    return supabase.table("notifications").select("*").eq("mosque_id",mosqueId).order("created_at", desc = True).execute()
    

def updateNotification(notificationId:str, data: dict):
    supabase.table("notifications").update(data).eq("notification_id", notificationId).execute()
    return {
        "message" : "Notification Updated Successfully"
    }
    
def deleteNotification(notificationId : str):
    supabase.table("notifications").delete().eq("notification_id",notificationId).execute()
    
    return {
        "message" : "Notification Deleted Successfully"
    }