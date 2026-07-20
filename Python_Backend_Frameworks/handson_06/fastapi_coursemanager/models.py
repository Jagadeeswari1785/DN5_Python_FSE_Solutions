from sqlalchemy import Column, Integer, String
from database import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    code = Column(String(20), unique=True)
    credits = Column(Integer)
    department_id = Column(Integer)