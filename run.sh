#!/usr/bin/env bash
exec gunicorn -b :8000 foobar:app
