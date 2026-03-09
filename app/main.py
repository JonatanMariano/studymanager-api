from fastapi import FastAPI
from .database.connection import Base, engine

from .models import user, course, enrollment

from .controllers import user_controller
from .controllers import course_controller
from .controllers import enrollment_controller

app = FastAPI(title="StudyManager API")


Base.metadata.create_all(bind=engine)


app.include_router(user_controller.router)
app.include_router(course_controller.router)
app.include_router(enrollment_controller.router)


@app.get("/")
def root():
    return {"message": "StudyManager API running"}