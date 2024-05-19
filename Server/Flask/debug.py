import json

input_filename = 'data.json'

try:
    # Inhalte aus drone.json lesen
    with open(input_filename, 'r', encoding='utf-8') as infile:
        drone_data = json.load(infile)
    print("Inhalt der Datei:")
    print(json.dumps(drone_data, indent=4))
except FileNotFoundError:
    print(f"Die Datei {input_filename} wurde nicht gefunden.")
except json.JSONDecodeError as e:
    print(f"Fehler beim Lesen der JSON-Daten: {e}")
except Exception as e:
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")