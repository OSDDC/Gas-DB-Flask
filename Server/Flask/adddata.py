import json

def main():
    # Lese die vorhandene data.json-Datei ein
    try:
        with open('data.json', 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        print("Die Datei 'data.json' wurde nicht gefunden. Bitte erstelle sie zuerst.")
        return

    # Benutzereingabe für neue Daten
    data = input("Add new data: ")


    # Füge die neuen Daten zur vorhandenen Liste hinzu
    new_entry = {data}
    existing_data.append(new_entry)

    # Schreibe die aktualisierten Daten zurück in die data.json-Datei
    with open('data.json', 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

    print(f"Die Daten wurden erfolgreich zur 'data.json' hinzugefügt:\n{new_entry}")

if __name__ == "__main__":
    main()
