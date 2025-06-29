# wait_for_db.py
import os
import time
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

print("DB Waiter: Starting up...")

# Get the database URL from the environment
db_url = os.environ.get("DATABASE_URL")
if not db_url:
    print("DB Waiter: DATABASE_URL not found, exiting.")
    exit(1)

print(f"DB Waiter: Attempting to connect to the database...")

# Loop until a connection is successful
while True:
    try:
        # Try to create an engine and establish a connection
        engine = create_engine(db_url)
        connection = engine.connect()
        # If we get here, the connection was successful
        connection.close() # Close the connection immediately
        break # Exit the loop
    except OperationalError as e:
        print(f"DB Waiter: Connection failed - {e}. Retrying in 1 second...")
        time.sleep(1) # Wait for 1 second before trying again

print("DB Waiter: Database is ready!")