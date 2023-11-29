import json
import random
from datetime import datetime, timedelta

# Funktion zur Generierung von Dummy-Daten
def generate_dummy_data(num_entries):
    data = []
    start_date = datetime(2021, 1, 22)

    for i in range(num_entries):
        date = (start_date + timedelta(days=i)).strftime("%d.%m.%Y")
        entry = {
            "date": date,
            "ort": random.choice(["Mannheim", "Ludwigshafen", "Weinheim", "Heidelberg", "Neustadt"]),
            "CO": random.randint(1, 6),
            "NO2": random.randint(6, 9),
            "C2H5OH": random.randint(1, 7),
            "H2": random.randint(5, 15),
            "NH3": random.randint(10, 20),
            "CH4": random.randint(10, 15),
            "C3H8": random.randint(40, 50),
            "C4H10": random.randint(20, 30),
            "LPG": random.randint(1, 8),
            "GPL": random.randint(0, 12),
            "UVA": random.randint(1, 10),
            "UVB": random.randint(1, 10),
            "%": random.randint(10, 100),
            "TEMP": random.randint(25, 32),
        }
        data.append(entry)

    return data

# Anzahl der Dummy-Einträge
num_entries = 30

# Dummy-Daten generieren
dummy_data = generate_dummy_data(num_entries)

# Dummy-Daten in JSON-Datei speichern
json_file_path = 'data.json'
with open(json_file_path, 'w') as file:
    json.dump(dummy_data, file, indent=2)

print(f'Dummy-Daten wurden erfolgreich in "{json_file_path}" gespeichert.')
