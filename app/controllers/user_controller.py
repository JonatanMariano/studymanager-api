from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database.connection import get_db
from ..schemas.user_schema import UserCreate
from ..services import user_service

router = APIRouter()


@router.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    try:
        new_user = user_service.create_user(db, user.name, user.email)

        return {
            "success": True,
            "message": "User created successfully",
            "data": new_user
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/users")
def list_users(db: Session = Depends(get_db)):

    users = user_service.get_users(db)

    return {
        "success": True,
        "message": "Users retrieved",
        "data": users
    }


@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):

    try:
        user = user_service.get_user_by_id(db, user_id)

        return {
            "success": True,
            "message": "User retrieved",
            "data": user
        }

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):

    try:
        updated = user_service.update_user(
            db,
            user_id,
            user.name,
            user.email
        )

        return {
            "success": True,
            "message": "User updated",
            "data": updated
        }

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):

    try:
        deleted = user_service.delete_user(db, user_id)

        return {
            "success": True,
            "message": "User deleted",
            "data": deleted
        }

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))