### Code "steuern" ###

spielAktiv = False
# "if"-Abfragen überprüfen ob etwas dem angebenen Wert entspricht
# und falls ja wird der code innerhalb der if abfrage ausgeführt
# wenn nicht dann wird es einfach übersprungen

if spielAktiv == True:
    print("Das spiel ist gestartet")
# mit "else" kann mann "oder" deffinieren
# if/else = entweder / oder
else:
    print("Spiel ist nicht gestartet!")
    
    
# Schleifen wie "for"/"while" sind weitere optionen
# "while" als "solange" etwas True (wahr) ist wird der code ausgeführt

counter = 10
while counter >= 0:
    print(f"Counter ist: {counter}")
    counter -= 1
