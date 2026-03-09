from pydantic import BaseModel


class CourseCreate(BaseModel):
    title: str
    description: str
    workload: int


class CourseResponse(BaseModel):
    id: int
    title: str
    description: str
    workload: int

    class Config:
        from_attributes = True