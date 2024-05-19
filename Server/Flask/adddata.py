import json

try:
    with open('drone.json', 'r') as input:
        data_drone = json.load(input)
except FileNotFoundError:
    print("Die Datei 'data.json' wurde nicht gefunden. Bitte erstelle sie zuerst.")

data = []
data.append(data_drone)



# Schreibe die aktualisierten Daten zurück in die data.json-Datei
with open('data.json', 'w') as output:
    json.dump(data, output, indent=2)

print(f"Die Daten wurden erfolgreich zur 'data.json' hinzugefügt:\n{new_entry}")
