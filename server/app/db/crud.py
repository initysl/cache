"""Database CRUD operations"""
from sqlalchemy.orm import Session
from . import models

def create_document(db: Session, title: str, content_hash: str):
    doc = models.Document(title=title, content_hash=content_hash)
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc
