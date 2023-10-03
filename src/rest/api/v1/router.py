from fastapi import APIRouter

from src.rest.api.v1.user import router as user_router
from src.rest.api.v1.book import router as book_router

router = APIRouter()

router.include_router(user_router, prefix='/v1')
router.include_router(book_router, prefix='/v1')

