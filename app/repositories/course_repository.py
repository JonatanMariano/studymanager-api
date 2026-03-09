from sqlalchemy.orm import Session
from ..models.course import Course


def create_course(db: Session, title: str, description: str, workload: int):

    course = Course(
        title=title,
        description=description,
        workload=workload
    )

    db.add(course)
    db.commit()
    db.refresh(course)

    return course


def get_courses(db: Session):
    return db.query(Course).all()


def get_course_by_id(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()


def update_course(db: Session, course_id: int, title: str, description: str, workload: int):

    course = get_course_by_id(db, course_id)

    if not course:
        return None

    course.title = title
    course.description = description
    course.workload = workload

    db.commit()
    db.refresh(course)

    return course


def delete_course(db: Session, course_id: int):

    course = get_course_by_id(db, course_id)

    if not course:
        return None

    db.delete(course)
    db.commit()

    return course