"""Database models for metadata tables"""
from sqlalchemy import Column, Integer, String, DateTime
from .postgres import Base

class Document(Base):
    __tablename__ = "documents"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content_hash = Column(String, unique=True)
