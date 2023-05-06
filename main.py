from fastapi import FastAPI

blog = FastAPI()

@blog.get("/")
async def home():
    return {'message': 'hello, welcome to my website :)'}

