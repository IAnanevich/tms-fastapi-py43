from fastapi import APIRouter

router = APIRouter()


@router.get('/books')
def get_books():
    return {'books': 'book1'}
