from fastapi import FastAPI
from routes.auth_routes import router as auth_router

app = FastAPI(
    title= "MyMasjid",
    version="0.0.1"
)

app.include_router(auth_router)


@app.get("/")
def health_check():
    return {
        "status" : "OK",
        "message": "My Masjid backend is Running"
    }