import locale
locale.setlocale(locale.LC_ALL, 'de_DE')

preis = input("Bitte den Preis eingeben: ")
rabatt_in_prozent = input("Bitte Rabatt in % angeben: ")
preis = locale.atof(preis)
rabatt_in_prozent = locale.atof(rabatt_in_prozent)
rabatt_in_euro = preis/100 * rabatt_in_prozent
preis_neu = preis - rabatt_in_euro
print("Preis mit", locale.format_string('%.2f', rabatt_in_prozent), "% Rabatt ist", locale.format_string('%.2f', preis_neu), "€")

zahlung = input("Der Kunde zahlt: ")
zahlung = locale.atof(zahlung)
rueckgeld = zahlung - preis_neu
print("Gegeben:", locale.format_string('%.2f', zahlung), "€ Preis:", locale.format_string('%.2f', preis_neu), "€")
print("Wechselgeld:", locale.format_string('%.2f', rueckgeld))
