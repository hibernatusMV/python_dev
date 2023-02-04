""" Class for database transctions """
import sqlite3
import os

class database:
    """ connection to database """
    data = ""

    def execQuery(query):
        # print(os.getcwd())
        with sqlite3.connect("database/observationlog.db") as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            database.data = cursor.fetchall()
