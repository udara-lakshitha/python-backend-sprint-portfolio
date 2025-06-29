# database.py
import os
from sqlmodel import create_engine, SQLModel, Session
from dotenv import load_dotenv

# This line will find the .env file and load its contents
# into the environment for this script.
load_dotenv()

# Get the database URL from the environment variables
DATABASE_URL = os.environ.get("DATABASE_URL")

# A crucial check to ensure the variable was loaded correctly,
# preventing the 'got None' error.
if not DATABASE_URL:
    raise ValueError("FATAL: DATABASE_URL environment variable is not set.")

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
