# database.py
import os
from sqlmodel import create_engine, SQLModel, Session

# Get the database URL from the environment variables we set in docker-compose
DATABASE_URL = os.environ.get("DATABASE_URL")

# Create the database engine. The 'connect_args' are recommended for SQLite,
# but are not needed for PostgreSQL. We can leave them out.

engine = create_engine(DATABASE_URL)

# This function is the one we will call to create the tables.
def create_db_and_tables():
    print("Creating database and tables...")
    SQLModel.metadata.create_all(engine)
    print("Database and tables created successfully.")

# This is a "dependency" function. FastAPI will run this for every
# request that needs a database connection.
def get_session():
    with Session(engine) as session:
        yield session
