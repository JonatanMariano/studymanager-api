from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime
from ..database.connection import Base


class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    course_id = Column(Integer, ForeignKey("courses.id"))

    enrolled_at = Column(DateTime, default=datetime.utcnow)