from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database.connection import get_db
from ..schemas.course_schema import CourseCreate
from ..services import course_service

router = APIRouter()


@router.post("/courses")
def create_course(course: CourseCreate, db: Session = Depends(get_db)):

    new_course = course_service.create_course(
        db,
        course.title,
        course.description,
        course.workload
    )

    return {
        "success": True,
        "message": "Course created",
        "data": new_course
    }


@router.get("/courses")
def list_courses(db: Session = Depends(get_db)):

    courses = course_service.get_courses(db)

    return {
        "success": True,
        "message": "Courses retrieved",
        "data": courses
    }


@router.get("/courses/{course_id}")
def get_course(course_id: int, db: Session = Depends(get_db)):

    try:
        course = course_service.get_course_by_id(db, course_id)

        return {
            "success": True,
            "message": "Course retrieved",
            "data": course
        }

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/courses/{course_id}")
def update_course(course_id: int, course: CourseCreate, db: Session = Depends(get_db)):

    try:
        updated = course_service.update_course(
            db,
            course_id,
            course.title,
            course.description,
            course.workload
        )

        return {
            "success": True,
            "message": "Course updated",
            "data": updated
        }

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/courses/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):

    try:
        deleted = course_service.delete_course(db, course_id)

        return {
            "success": True,
            "message": "Course deleted",
            "data": deleted
        }

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))