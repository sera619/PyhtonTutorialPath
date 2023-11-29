### USER EINGABEN ###
# einen Wert oder 'Daten' vom user erfragen
userInput = input("Bitte gebe etwas ein: ")
print(f"Deine Eingabe war:\n'{userInput}'")

# Beispiel basic telefonbuch mit name, telefonnummer

# initialisieren der benötigten variablen (Listen, Dicts etc.)
telefonbuch = []
newName = input("Gebe einen Namen ein: ")
newPhone = int(input("Gebe die Telefonummer ein (Zahlen): "))

newKontakt = {
    "Name": newName,
    "Telefon": newPhone
}
telefonbuch.append(newKontakt)
print(f"Ein neuer Kontakt: '{newKontakt['Name']}' erstellt.")

for contact in telefonbuch:
    print(f"Name: '{contact['Name']}' | Telefon: {contact['Telefon']}")