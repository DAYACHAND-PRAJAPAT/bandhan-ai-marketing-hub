from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.auth import router as auth_router
from app.api.v1.leads import router as lead_router

app = FastAPI(
    title="Bandhan AI Marketing Hub API",
    description="Backend API for Bandhan AI Marketing Hub",
    version="1.0.0",
)

app.include_router(
    auth_router,
    prefix="/api/v1",
)
app.include_router(lead_router, prefix="/api/v1")


origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Bandhan AI Marketing Hub API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }