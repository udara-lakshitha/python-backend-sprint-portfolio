# wait_for_db.py
import os
import time
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

print("DB Waiter: Starting...")

retries = 15
while retries > 0:
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        print(f"DB Waiter: DATABASE_URL not set. Waiting... ({retries} retries left)")
        time.sleep(2)
        retries -= 1
        continue

    try:
        print("DB Waiter: Attempting to connect...")
        engine = create_engine(db_url)
        with engine.connect():
            print("DB Waiter: Database connection successful!")
            # Exit the script with a success code
            exit(0)
    except OperationalError:
        print(f"DB Waiter: Connection failed. Retrying... ({retries} retries left)")
        time.sleep(2)
        retries -= 1

print("DB Waiter: FATAL - Could not connect to database. Exiting.")
# Exit the script with a failure code
exit(1)