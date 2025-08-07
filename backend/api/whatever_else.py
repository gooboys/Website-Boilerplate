from fastapi import APIRouter

router = APIRouter(prefix="/stuff")

@router.get("/")
def get_stuff():
    return {"message": "Here's your stuff"}