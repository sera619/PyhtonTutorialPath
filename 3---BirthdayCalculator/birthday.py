import datetime, os, sys
from colorama import init, Fore

def get_user_birthday():
    try:
        # frage nutzer nach geburts-tag
        tag = int(input(Fore.YELLOW + "[?] Gebe dein Geburts-Tag ein [DD]: " + Fore.RESET))
        if not 1 <= tag <= 31:  
            raise ValueError("Ungültiger Tag")
        # frage nutzer nach geburts-monat
        monat = int(input(Fore.YELLOW+"[?] Gebe dein Geburts-Monat ein [MM]: "+Fore.RESET))
        if not 1 <= monat <= 12:
            raise ValueError("Ungültiger Monat")
        # frage nutzer nach geburts-jahr
        jahr = int(input(Fore.YELLOW+"[?] Gebe dein Geburts-Jahr ein [YYYY]: "+Fore.RESET))
        if not 1900 < jahr <= 2023:
            raise ValueError("Ungültiges Jahr")
        # wandle eingaben in ein "datetime"-object um
        geburtstag = datetime.datetime(jahr, monat, tag)
        # gebe geburtsdatum zurück
        return geburtstag
    # sollte eine eingabe ungültig sein wird der entstandene
    # Fehler zurück gegeben inklusive des error-codes
    except ValueError as e:
        print(Fore.RED +f"[X] Fehler: {e}"+ Fore.RESET)
        return get_user_birthday()
    
def calculate_dates(original_date, now):
    # Berechne den nächsten Geburtstag im aktuellen Jahr und im nächsten Jahr
    delta1 = datetime.datetime(now.year, original_date.month, original_date.day)
    delta2 = datetime.datetime(now.year + 1, original_date.month, original_date.day)
    # Berechne die verbleibenden Tage bis zum nächsten Geburtstag
    return ((delta1 if delta1 > now else delta2) - now).days

def calculate_age_and_name(birthday, now):
    # Berechne das Alter des Benutzers
    age = now.year - birthday.year - ((now.month, now.day) < (birthday.month, birthday.day))
    # Finde den Namen des Wochentags des nächsten Geburtstags
    next_birthday_weekday = birthday.replace(year=now.year)  # Setze das Jahr auf das aktuelle Jahr
    weekday_name = next_birthday_weekday.strftime("%A")  # Formatieren des Wochentagsnamens
    return age, weekday_name

def main():
    # Löscht die Konsole (funktioniert auf Windows)
    os.system("cls")
    # Initialisiert das Colorama-Modul für farbigen Text
    init() 
    print(Fore.RED +"Geburtstagsrechner mit Python\n\n"+Fore.CYAN+"Dieses kleine Tool rechnet die verbleibenden Tage\nbis zu deinem nächsten Geburtstag aus.\n"
          + Fore.BLUE + "\nCTRL+X zum Beenden.\n\n" + Fore.RESET)
    # Ruft die Funktion auf, um den Geburtstag des Benutzers zu erhalten
    birthday = get_user_birthday()
    # Aktuelles Datum und Uhrzeit
    now = datetime.datetime.now()
    # Berechnet die verbleibenden Tage bis zum nächsten Geburtstag
    next_birthday = calculate_dates(birthday, now)
    # Berechnet das Alter und den Namen des Wochentags des nächsten Geburtstags
    age, weekday_name = calculate_age_and_name(birthday, now) 
    # gibt die Ergebnisse als Textausgabe an den Benutzer zurück
    print(Fore.GREEN + f"\n[!] Dein nächster Geburtstag ist in " + Fore.RED + f"{next_birthday}" + Fore.GREEN + " Tagen.\n"
          f"[!] Du wirst "+Fore.RED + f"{age}" + Fore.GREEN + " Jahre.\n"
          f"[!] Dein Geburtstag wird an einem "+ Fore.RED + f"{weekday_name}"+ Fore.GREEN+ " sein.\n" + Fore.RESET)
# startet das programm 
if __name__ == '__main__':
    try:
        main()
    # wenn ctrl+x gedrückt wird programm ohne fehler beendet
    except KeyboardInterrupt as e:
        sys.exit()

