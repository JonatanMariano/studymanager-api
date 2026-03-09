from sqlalchemy.orm import Session
from ..repositories import enrollment_repository
from ..repositories import user_repository
from ..repositories import course_repository


def create_enrollment(db: Session, user_id: int, course_id: int):

    user = user_repository.get_user_by_id(db, user_id)

    if not user:
        raise ValueError("User does not exist")

    course = course_repository.get_course_by_id(db, course_id)

    if not course:
        raise ValueError("Course does not exist")

    existing = enrollment_repository.get_enrollment(db, user_id, course_id)

    if existing:
        raise ValueError("User already enrolled in this course")

    return enrollment_repository.create_enrollment(
        db,
        user_id,
        course_id
    )