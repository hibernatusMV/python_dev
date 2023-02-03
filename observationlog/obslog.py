from classes.database import database

database.execQuery("select * from observations")
print(database.data)