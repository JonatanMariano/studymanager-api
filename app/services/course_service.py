from sqlalchemy.orm import Session
from ..repositories import course_repository


def create_course(db: Session, title: str, description: str, workload: int):

    return course_repository.create_course(
        db,
        title,
        description,
        workload
    )


def get_courses(db: Session):

    return course_repository.get_courses(db)


def get_course_by_id(db: Session, course_id: int):

    course = course_repository.get_course_by_id(db, course_id)

    if not course:
        raise ValueError("Course not found")

    return course


def update_course(db: Session, course_id: int, title: str, description: str, workload: int):

    course = course_repository.update_course(
        db,
        course_id,
        title,
        description,
        workload
    )

    if not course:
        raise ValueError("Course not found")

    return course


def delete_course(db: Session, course_id: int):

    course = course_repository.delete_course(db, course_id)

    if not course:
        raise ValueError("Course not found")

    return course