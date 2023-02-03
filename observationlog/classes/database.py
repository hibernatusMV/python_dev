""" Class for database transctions """
import sqlite3
import os

class database:
    """ connection to database """
    data = ""

    def execQuery(query):
        # print(os.getcwd())
        conn = sqlite3.connect("database/observationlog.db")

        cursor = conn.cursor()
        cursor.execute(query)
        database.data = cursor.fetchall()
        
        conn.commit()
        conn.close()
