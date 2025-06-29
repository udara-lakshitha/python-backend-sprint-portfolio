# models.py
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from pydantic import BaseModel

# --- The User Model ---
# Represents the 'user' table in our database
class User(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    username: str = Field(index = True, unique = True)
    hashed_password: str

    # This defines one-to-many relationship
    # One user can have many posts
    # The 'posts' attribute will be a list of Post object
    posts: List["Post"] = Relationship(back_populates = "user")

# --- The Post Model ---
class Post(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    text: str

    # This is the foreign key that links a Post back to a User.
    user_id: int = Field(foreign_key = "user.id")

    # This defines the other side of the one-to-many relationship.
    # Each post belongs to one user.
    # The 'user' attribute will be a User object.
    user: User = Relationship(back_populates = 'posts')

class PostCreate(BaseModel):
    text: str
    user_id: int

class PostRead(BaseModel):
    id: int
    text: str

class UserRead(BaseModel):
    id: int
    username: str

class UserReadWithPosts(BaseModel):
    id: int
    username: str
    posts: List[PostRead]

class PostReadWithUser(BaseModel):
    id: int
    text: str
    user: UserRead