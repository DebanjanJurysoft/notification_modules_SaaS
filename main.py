from fastapi import FastAPI
from app import router as app_router

app = FastAPI(
    title='Notification Module',
    version='1.0.0',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(app_router)


