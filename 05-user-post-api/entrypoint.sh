#!/bin/sh

# This entrypoint script first runs our Python database waiter,
# and only then executes the main container command.

# Run the waiter script
python wait_for_db.py

# Execute the main command (e.g., uvicorn) passed to this script
exec "$@"