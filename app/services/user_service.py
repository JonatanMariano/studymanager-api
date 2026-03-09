from sqlalchemy.orm import Session
from ..repositories import user_repository
from ..models.user import User


def create_user(db: Session, name: str, email: str):

    existing_user = db.query(User).filter(User.email == email).first()

    if existing_user:
        raise ValueError("Email already registered")

    return user_repository.create_user(db, name, email)


def get_users(db: Session):

    return user_repository.get_users(db)


def get_user_by_id(db: Session, user_id: int):

    user = user_repository.get_user_by_id(db, user_id)

    if not user:
        raise ValueError("User not found")

    return user


def update_user(db: Session, user_id: int, name: str, email: str):

    user = user_repository.update_user(db, user_id, name, email)

    if not user:
        raise ValueError("User not found")

    return user


def delete_user(db: Session, user_id: int):

    user = user_repository.delete_user(db, user_id)

    if not user:
        raise ValueError("User not found")

    return user