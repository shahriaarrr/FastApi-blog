from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from routes import blog_get, blog_post, user, article
from db import models
from db.database import engine
from exceptions import EmailNotValid

blog = FastAPI()

blog.include_router(blog_get.router)
blog.include_router(blog_post.router)
blog.include_router(user.router)
blog.include_router(article.router)

# create database with our Engine
models.Base.metadata.create_all(engine)


@blog.get("/", description="this is the Home page of out blog")
async def home():
    return {'message': 'hello, welcome to my website :)'}


@blog.exception_handler(EmailNotValid)
def email_not_vaild(request: Request, exc: EmailNotValid):
    return JSONResponse(content=str(exc), status_code=status.HTTP_400_BAD_REQUEST)
