#!/bin/sh

# This is our universal entrypoint script.

# We will poll the database to see if it's ready.
# The 'pg_isready' command is a standard PostgreSQL utility.
# We must install its client package in our Dockerfile.

# We don't need to parse the URL here. The 'pg_isready' command
# can take the full DATABASE_URL as an argument.
echo "Waiting for database to be ready..."

# Loop until the database is ready to accept connections
until pg_isready -h db -p 5432 -U user; do
  echo "  ... database is not ready, waiting 1 second"
  sleep 1
done

echo "Database is ready! Starting application..."

# Now, execute the main command that was passed to this script
# (e.g., 'uvicorn app:app ...')
exec "$@"