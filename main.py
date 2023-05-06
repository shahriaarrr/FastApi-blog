from fastapi import FastAPI

blog = FastAPI()

@blog.get("/", description="this is the Home page of out blog")
async def home():
    return {'message': 'hello, welcome to my website :)'}

