#### AUSGABE ####
# jede variable (folgend) kann in der konsole ausgegben werden
print()

# hier folgend int, float, bool, string variablen
myInt = 2
myFloat = 3.22
myBool = False
myString = "Hello World!"

######## ignore ########
ml = [myInt, myFloat, myBool, myString]
for i in ml:
    print(f"Ich bin der datentyp: {type(i)} und habe den Wert: {i}!")
########################

# mathemathisches arbeiten mit zahlen
print("Addition:\n2 + 3 = ", 2 + 3)
print("Subtraktion:\n10 - 7 = ", 10 - 7)
print("Multiplizieren:\n2 * 2 = ", 2 * 2)
print("Dividieren:\n20 / 5 = ", 20 / 5)

# daten speichern in listen oder dictionarys 
myList = ["Ich", "bin", "eine", "Liste"]
myDictionary = {
    "Name": "S3R43o3",
    "Alter": 33,
    "Email": "Seraphinus619@gmail.com" 
}

# etwas zu einer liste hinzufügen
myList.append("!")
# durch eine liste loopen ("scrollen") 
for j in myList:
    # jedes einzelne element in der liste ausgeben
    print(j)
# das letzte item aus der liste löschen und den wert zurück geben
letzterEintrag = myList.pop()
print(f"Dies war der letzte Listeneintrag:\n{letzterEintrag}")
# "zählen" wieviele Einträge eine liste hat:
print(f"Die Liste hat '{len(myList)}' Einträge!")

# jeden Key und den Wert aus dem dictionary "myDictrionary" ausgeben:
for key, value in myDictionary.items():
    print(f"Das ist der key: '{key}' mit dem Wert: '{value}'")
