from enum import Enum
from sqlalchemy import Column, Integer, String, Boolean, Enum as SQLAlchemyEnum, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class UserRoleEnum(str, Enum):
    job_seeker = "job_seeker"
    employer = "employer"

    def __str__(self):
        return str(self.value)

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(SQLAlchemyEnum(UserRoleEnum))  # Use SQLAlchemy Enum type here

class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    job_title = Column(String)
    # Define other fields as needed

    user = relationship("UserDB", back_populates="job_applications")

UserDB.job_applications = relationship("JobApplication", back_populates="user")