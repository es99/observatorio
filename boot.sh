#!/bin/bash
. venv/bin/activate

while true; do
    flask db upgrade
    if [ "$?" -eq 0 ]; then
        break
    fi
    echo "flask db upgrade failed, retrying in 5 secs..."
    sleep 5
done

gunicorn -b 0.0.0.0:9000 flasky:app