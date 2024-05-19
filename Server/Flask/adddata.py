import json

# Dateinamen
input_filename = 'drone.json'
output_filename = 'data.json'

def validate_json(content):
    try:
        json.loads(content)
        return True
    except json.JSONDecodeError:
        return False

try:
    # Inhalte aus drone.json lesen
    with open(input_filename, 'r', encoding='utf-8') as infile:
        content = infile.read()
        if not validate_json(content):
            raise ValueError("Ungültiges JSON-Format in der Datei.")
        drone_data = json.loads(content)

    # Inhalte in eine Liste packen
    data_to_write = [drone_data]

    # Inhalte in data.json schreiben
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        json.dump(data_to_write, outfile, ensure_ascii=False, indent=2)

    print(f"Die Daten aus {input_filename} wurden erfolgreich in {output_filename} geschrieben.")

except FileNotFoundError:
    print(f"Die Datei {input_filename} wurde nicht gefunden.")
except json.JSONDecodeError as e:
    print(f"Fehler beim Lesen der JSON-Daten: {e}")
except ValueError as e:
    print(e)
except Exception as e:
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")