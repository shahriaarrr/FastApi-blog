from sqlalchemy.orm.session import Session
from schemas import ArticleBase
from db.models import DBArticle
from fastapi import status
from fastapi.exceptions import HTTPException

def create_article(db: Session, request: ArticleBase):
    article = DBArticle(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=request.creator_id,
    )
    db.add(article)
    db.commit()
    db.refresh(article)

    return article

def get_article(id, db: Session):
    article = db.query(DBArticle).filter(DBArticle.id == id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"article number {id} not found!!",
        )

    return article