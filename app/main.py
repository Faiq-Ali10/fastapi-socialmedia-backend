from fastapi import FastAPI
from . import models
from .database import engine
from app.routes.posts import router as post_router
from app.routes.users import router as user_router
from app.routes.auth import router as auth_router
from app.routes.votes import router as vote_router
from fastapi.middleware.cors import CORSMiddleware
import os

# if os.getenv("ENV") != "test":
#     models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(vote_router)

@app.get("/")
async def root():
    return {"message":"Hello world, if you want to use Swagger UI go to /docs further"}
