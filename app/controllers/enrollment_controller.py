from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database.connection import get_db
from ..schemas.enrollment_schema import EnrollmentCreate
from ..services import enrollment_service
from ..repositories import enrollment_repository, course_repository, user_repository

router = APIRouter()


@router.post("/enrollments")
def create_enrollment(enrollment: EnrollmentCreate, db: Session = Depends(get_db)):

    try:
        result = enrollment_service.create_enrollment(
            db,
            enrollment.user_id,
            enrollment.course_id
        )

        return {
            "success": True,
            "message": "Enrollment created",
            "data": result
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/users/{user_id}/courses")
def get_user_courses(user_id: int, db: Session = Depends(get_db)):

    user = user_repository.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    enrollments = enrollment_repository.get_user_enrollments(db, user_id)

    courses = []

    for enrollment in enrollments:

        course = course_repository.get_course_by_id(
            db,
            enrollment.course_id
        )

        courses.append({
            "id": course.id,
            "title": course.title
        })

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "courses": courses
    }