from sqlalchemy.orm.session import Session
from schemas import ArticleBase
from db.models import DBArticle

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


