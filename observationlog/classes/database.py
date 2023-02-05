""" Class for database transactions """
import sqlite3

class database:
    """ connection to database """
    data = {} # initialize array
    rowcount = 0

    def execQuery(query):
        """ retrieve data for specific select """
        with sqlite3.connect("database/observationlog.db") as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query)
            
                row = 0
                col = 0

                # shove values from tuple into array
                for dataset in cursor:
                    for value in dataset:
                        database.data[row,col] = value
                        col += 1
                    row += 1
                database.rowcount = row # rows retrieved
            
            except sqlite3.OperationalError:
                print("Tabelle nicht gefunden!")
            except:
                print("Daten konnten nicht verarbeitet werden!")

    def rowcount(query):
        with sqlite3.connect("database/observationlog.db") as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(query)
                database.rowcount = cursor.fetchone()
            
            except sqlite3.OperationalError:
                print("Tabelle nicht gefunden!")
            except:
                print("Daten konnten nicht verarbeitet werden!")