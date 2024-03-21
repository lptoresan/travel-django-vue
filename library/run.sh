#!/bin/bash

# Commands to run
COMMANDS=(
    "cd /library && python manage.py runserver"
    "cd /library/vueweb/travelapp && npm run serve"
)

# Execute commands locally
for cmd in "${COMMANDS[@]}"; do
    eval "$cmd"
done