#!/usr/bin/env python3
""" Basic application for test Jenkins, Docker, """
import sqlite3
import json

def app(env, start_response):
    """ Test application. Return list of users in JSON format on HTTP proto"""
    #pylint: disable=unused-argument
    data = get_users().encode('utf-8')
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])

def get_users():
    """ Get user list from sqlite3 DB. Return json """
    con = sqlite3.connect('shosser.db')
    cur = con.cursor()
    query = 'SELECT * FROM users;'
    result = cur.execute(query)
    users = [dict(zip([key[0] for key in cur.description], row)) for row in result]
    return json.dumps({'users': users})
