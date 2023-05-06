from db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class DBUser(Base):
    __tablename__ = 'users'

    id = Column(Integer, index=True, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship('DBArticle', back_populates='user')



class DBArticle(Base):
    __tablename__ = 'articles'

    id = Column(Integer, index=True, primary_key=True)
    title = Column(String)
    content = Column(String)
    published = Column(Boolean)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('DBUser', back_populates='items')
