from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from database import Base 

class User(Base):
    __tablename__ = "User"
    
    id: Mapped[str] = mapped_column(String(36), primary_key = True)
    name: Mapped[str] = mapped_column(String(36), nullable=False)
    email: Mapped[str] = mapped_column(String(64), nullable=False, unique= True)
    password: Mapped[str] = mapped_column(String(64), nullable=False)
    memo: Mapped[str] = mapped_column(String(64), nullable=True)
    created_at: Mapped[str] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[str] = mapped_column(DateTime, nullable=False)