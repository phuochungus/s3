#!/bin/bash
# entrypoint.sh

# Exit immediately if a command exits with a non-zero status.
set -e

# Start the server with the specified port
exec python manage.py runserver 0.0.0.0:${PORT}
