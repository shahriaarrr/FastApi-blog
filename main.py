from fastapi import FastAPI

from routes import blog_get
from db import models
from db.database import engine

blog = FastAPI()

blog.include_router(blog_get.router)

#create database with our Engine
models.Base.metadata.create_all(engine)

@blog.get("/", description="this is the Home page of out blog")
async def home():
    return {'message': 'hello, welcome to my website :)'}

