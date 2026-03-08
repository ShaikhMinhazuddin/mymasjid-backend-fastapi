from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.auth_routes import router as auth_router

app = FastAPI(
    title= "MyMasjid",
    version="0.0.1"
)
# --- CORS CONFIGURATION ---
app.add_middleware(
    CORSMiddleware,
    # This allows your Vite frontend (default port 5173) to connect
    allow_origins=[
        "http://localhost:5173", 
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Allows POST, GET, PUT, DELETE, etc.
    allow_headers=["*"],  # Allows all headers (Content-Type, Authorization, etc.)
)

app.include_router(auth_router)


@app.get("/")
def health_check():
    return {
        "status" : "OK",
        "message": "My Masjid backend is Running"
    }