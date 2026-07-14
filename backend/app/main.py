from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Bandhan AI Marketing Hub API",
    description="Backend API for Bandhan AI Marketing Hub",
    version="1.0.0",
)

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