'''FastAPI endpoints'''
from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker

from schemas import UserBaseSchema, PostBaseSchema
from tables import Base, Post, User


app = FastAPI()

url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="1956",
    host="localhost",
    port=5432,
    database="py_lab9",
)

engine = create_engine(url)

Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)
db = session()


@app.get("/")
def redirect_to_docs():
    '''Redirect from root to Swagger docs'''
    return RedirectResponse("/docs")


# user CRUD methods
@app.get("/user")
def get_user(id):
    '''Return a User entry'''
    user: User
    try:
        user = db.query(User).get(id)
    except Exception:
        return Response(f"User with id {id} not found", status_code=404)
    return user


@app.post("/user")
def create_user(payload: UserBaseSchema):
    '''Create a User entry'''
    user = User(**payload.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@app.put("/user")
def update_user(payload: UserBaseSchema):
    '''Update a User entry'''
    user: User
    try:
        user = db.query(User).get(id)
    except Exception:
        return Response(f"User with id {payload.id} not found", status_code=404)

    db.query(User) \
        .filter(User.id == user.id) \
        .update({User.username: user.username,
                 User.email: user.email,
                 User.password: user.password})
    db.commit()
    return user


@app.delete("/user")
def delete_user(id):
    '''Delete a User entry'''
    user: User
    try:
        user = db.query(User).get(id)
    except Exception:
        return Response(f"User with id {id} not found", status_code=404)

    db.delete(user)
    db.commit()
    db.refresh(user)

    return user


# post CRUD methods
@app.get("/post")
def get_post(id):
    '''Get a Post entry'''
    post: Post
    try:
        post = db.query(Post).get(id)
    except Exception:
        return Response(f"Post with with id {id} not found", status_code=404)
    return post


@app.post("/post")
def create_post(payload: PostBaseSchema):
    '''Create a Post entry'''
    post = Post(**payload.model_dump())
    db.add(post)
    db.commit()
    db.refresh(post)

    return post


@app.put("/post")
def update_post(payload: PostBaseSchema):
    '''Update a Post entry'''
    post: Post
    try:
        post = db.query(Post).get(id)
    except Exception:
        return Response(f"Post with with id {payload.id} not found", status_code=404)

    db.query(Post) \
        .filter(Post.id == post.id) \
        .update({Post.title: post.title,
                 Post.content: post.content})

    return post


@app.delete("/post")
def delete_post(id):
    '''Delete a Post entry'''
    post: Post
    try:
        post = db.query(Post).get(id)
    except Exception:
        return Response(f"Post with with id {id} not found", status_code=404)

    db.delete(post)
    db.commit()
    db.refresh(post)

    return post
