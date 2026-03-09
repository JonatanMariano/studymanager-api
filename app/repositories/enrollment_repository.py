from sqlalchemy.orm import Session
from ..models.enrollment import Enrollment


def create_enrollment(db: Session, user_id: int, course_id: int):

    enrollment = Enrollment(
        user_id=user_id,
        course_id=course_id
    )

    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)

    return enrollment


def get_enrollment(db: Session, user_id: int, course_id: int):

    return db.query(Enrollment).filter(
        Enrollment.user_id == user_id,
        Enrollment.course_id == course_id
    ).first()


def get_user_enrollments(db: Session, user_id: int):

    return db.query(Enrollment).filter(
        Enrollment.user_id == user_id
    ).all()