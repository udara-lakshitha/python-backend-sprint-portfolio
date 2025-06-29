# wait_for_db.py (Version 2)
import os
import time
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

print("DB Waiter: Starting up...")

db_url = None
retries = 10

# --- NEW: Retry loop to find the DATABASE_URL ---
print("DB Waiter: Looking for DATABASE_URL environment variable...")
while retries > 0:
    db_url = os.environ.get("DATABASE_URL")
    if db_url:
        print("DB Waiter: DATABASE_URL found!")
        break
    print(f"DB Waiter: DATABASE_URL not found. Retrying in 2 seconds... ({retries} retries left)")
    retries -= 1
    time.sleep(2)

if not db_url:
    print("DB Waiter: FATAL - DATABASE_URL not set after multiple retries. Exiting.")
    exit(1)

# --- Existing: Retry loop to connect to the database ---
print(f"DB Waiter: Attempting to connect to the database...")
retries = 10 # Reset retries for the connection
while retries > 0:
    try:
        engine = create_engine(db_url)
        with engine.connect() as connection:
            print("DB Waiter: Database connection successful.")
            break # Exit the loop
    except OperationalError as e:
        print(f"DB Waiter: Connection failed - {e}. Retrying in 2 seconds... ({retries} retries left)")
        retries -= 1
        time.sleep(2)

if retries == 0:
    print("DB Waiter: FATAL - Could not connect to database after multiple retries. Exiting.")
    exit(1)

print("DB Waiter: Database is ready!")
# The script will now exit with code 0, allowing the entrypoint to proceed.