#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Run the database waiter script.
# The 'set -e' above means if wait_for_db.py exits with an error (non-zero),
# this entire script will stop.
python wait_for_db.py

# If the waiter script succeeded, execute the main command passed to this entrypoint.
# This will be 'uvicorn app:app ...'
exec "$@"