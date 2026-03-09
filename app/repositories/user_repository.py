from sqlalchemy.orm import Session
from ..models.user import User

def create_user(db: Session, name: str, email: str):
    user = User(name=name, email=email)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user_id: int, name: str, email: str):

    user = get_user_by_id(db, user_id)

    if not user:
        return None

    user.name = name
    user.email = email

    db.commit()
    db.refresh(user)

    return user

def delete_user(db: Session, user_id: int):

    user = get_user_by_id(db, user_id)

    if not user:
        return None

    db.delete(user)
    db.commit()

    return user
