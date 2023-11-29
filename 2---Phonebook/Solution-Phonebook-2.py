import json
import sys

class Phonebook():
    def __init__(self):
        self.kontaktList = []
        self.loadContacts()
    
    def loadContacts(self):
        print("[!] Lade Konatkliste")
        data = None
        with open('./data/phonebook.json', 'r') as f:
            data = json.loads(f.read())        
        if data:
            print("[!] Kontaktliste geladen:\n")
            self.kontaktList = data
    
    def saveContact(self):
        if len(self.kontaktList) > 0:
            print("[!] Speichere Kontaktliste.")
            with open('./data/phonebook.json', 'w') as f:
                data = json.dumps(self.kontaktList)
                f.write(data)
        else:
            return
        
    def addContact(self, name, number):
        contact = {
            'Name': name,
            'Telefon': number
        }
        for c in self.kontaktList:
            if c['Name'] == name:
                print("[X] Kontakt bereits vorhanden!")
                return
        self.kontaktList.append(contact)
        self.saveContact()
        print(f"[!] Neuer Kontakt: {name} hinzugefügt!")
    
    def deleteContact(self, name):
        for contact in self.kontaktList:
            if contact['Name'] == name:
                self.kontaktList.remove(contact)
                self.saveContact()
                break

            
b = Phonebook()

def main():
    global b
    options = [
        "1) Kontakte anzeigen",
        "2) Kontakt hinzufügen",
        "3) Kontakt entfernen",
        "0) Exit"
    ]
    print("Telefonbuch Python\n")
    for o in options:
        print(o)
    option = int(input("\nOption: "))
    
    if option == 1:
        print("Deine Kontakte:\n")
        for i in b.kontaktList:
            print(f"# Name: {i['Name']}\n# Telefon: {i['Telefon']}\n#####################\n")
        main()
    elif option == 2:
        print("Neuer Kontakt:")
        newName = input("Gebe einen Namen ein: ")
        newPhone = input("Gebe eine Telefonnummer eine: ")
        b.addContact(newName, newPhone)
        main()
    elif option == 3:
        print("[!] Kontakt entfernen:")
        nameToDel = input("Gebe den Kontakt-Namen zum löschen ein: ")  
        b.deleteContact(nameToDel)
        main()
    elif option == 0:
        print("[!] Exit program, bye!")
        sys.exit()
    else:
        print("[X] Ungültige Eingabe, versuche es erneut!")
        main()
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as k:
        print("[X] User exit.")
    finally:
        sys.exit()