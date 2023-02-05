from classes.database import database

database.execQuery("select * from observations")
i = 0
rows = database.rowcount - 1

while i <= rows:
    print("Objekt: ", database.data[i,3], "Sternbild: ", database.data[i,7])
    i += 1