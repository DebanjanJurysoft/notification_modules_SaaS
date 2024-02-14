# app.py
from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def read_app():
    return {'message': 'Hello from Octopus'}

