from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from database import create_db_and_tables
from models import User, PostRead, PostCreate, Post, UserReadWithPosts, PostReadWithUser
from database import get_session
from typing import List
from sqlmodel import select, Session

# This is the new, modern way to handle startup/shutdown events in FastAPI
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("API is starting up...")
    create_db_and_tables() # Call our function to create tables
    yield
    print("API is shutting down...")

app = FastAPI(
    title =  "Monster's User & Post API",
    description = "A showcase of professional, database-driven backend",
    version = "1.0.0",
    lifespan = lifespan # Tell FastAPI to use our lifespan manager
)

@app.get("/")
def read_root():
    return {"status": "API is running!"}

# --- User Creation endpoint ---
@app.post("/users/", response_model = User)
def create_user(user: User, session: Session = Depends(get_session)):
    # Add the new user object to the session
    session.add(user)
    # Commit teh transaction to the database
    session.commit()
    # Refresh the user object to get the new ID from the database
    session.refresh(user)
    # Return the newly created user
    return user

# --- Read all users endpoint ---
@app.get('/users/', response_model = List[UserReadWithPosts])
def read_users(session: Session = Depends(get_session)):
    # Create a statement to select all users
    statement = select(User)
    # Execute the statement
    users = session.exec(statement).all()
    return users

# --- Create Posts Endpoint ---
@app.post('/posts/', response_model=PostReadWithUser)
def create_post(post: PostCreate, session: Session = Depends(get_session)):
    user_id = session.get(User, post.user_id)
    # Check the user id is exists
    if not user_id:
        raise HTTPException(status_code=404, detail="User with this ID not found.")
    # Create the database model instance directly from the input data
    post_to_db = Post(text=post.text, user_id=post.user_id)

    # Add, commit, refresh
    session.add(post_to_db)
    session.commit()
    session.refresh(post_to_db)

    return post_to_db

# --- Read posts endpoint ---
@app.get('/posts/', response_model=List[PostReadWithUser])
def read_posts(session: Session = Depends(get_session)):
    # Create a statement to select all posts
    statement = select(Post)
    # Execute the statement
    posts = session.exec(statement).all()
    return posts
