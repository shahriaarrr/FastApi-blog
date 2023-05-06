from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DBUser
from db.hash import Hash


def create_user(db: Session, request: UserBase):
    user = DBUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_all_users(db: Session):
    return db.query(DBUser).all()


def get_user(id, db: Session):
    user = db.query(DBUser).filter(DBUser.id == id).first()
    return user


def delete_user(id, db: Session):
    user = get_user(id, db)
    db.delete(user)
    db.commit()
    return 'OK'


def update_user(id, db: Session, request: UserBase):
    user = db.query(DBUser).filter(DBUser.id == id)
    user.update({
        DBUser.username: request.username,
        DBUser.email: request.email,
        DBUser.password: Hash.bcrypt(request.password),
    })
    db.commit()
    return 'OK'
