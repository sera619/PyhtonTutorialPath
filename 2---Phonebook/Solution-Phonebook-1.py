import json
import sys

dataPath = "./data/phonebook.json"

def loadContacts() -> list:
    data = None
    with open(dataPath, 'r') as f:
        data = json.loads(f.read())
    if data:
        return data

telefonBuch = loadContacts()

def getContacts():
    print("Deine Kontakte:\n")
    for i in telefonBuch:
        print(f"Name: {i['Name']}\nTelefon: {i['Telefon']}\n")

def addContact(name, number):
    contact = {
        'Name': name,
        'Telefon': number
    }
    telefonBuch.append(contact)
    print(f"[!] Neuer Kontakt '{name}' erstellt!")
    saveContact()
    
def deleteContact(name):
    for contact in telefonBuch:
        if contact['Name'] == name:
            print("Gefunden")
            telefonBuch.remove(contact)
            saveContact()
            break

def saveContact():
    with open(dataPath, 'w') as f:
        f.write(json.dumps(telefonBuch))
    print("[!] Telefonbuch gespeichert!")


def main():
    banner = "Telefonbuch Python"
    options = [
        "1) Kontakte anzeigen",
        "2) Kontakt hinzufügen",
        "3) Kontakt entfernen",
        "0) Exit"
    ]
    print(banner)
    for o in options:
        print(o)
    print("")
    option = int(input("Gebe eine Option ein: "))
    if option == 1:
        getContacts()
        main()
    elif option == 2:
        print("[!] Neuer Kontakt:")
        newName = input("Gebe einen Namen ein: ")
        newPhone = input("Gebe eine Telefonnummer ein: ")
        addContact(newName, newPhone)
        main()
    elif option == 3:
        print("[!] Kontakt entfernen:")
        nameToDel = input("Gebe den Kontakt-Namen zum löschen ein: ")
        deleteContact(nameToDel)
        main()
        
    elif option == 0:
        sys.exit()
    else:
        print("Die Eingabe war ungültig, versuche es nochmal!")
        main()


main()