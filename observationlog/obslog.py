from classes.database import database

database.execQuery("select * from observations")
database.rowcount("select count(*) from observations")
i = 0
row = database.rowcount[0] - 1

while i <= row:
    print("Objekt: ", database.data[i,3], "Sternbild: ", database.data[i,7])
    i += 1