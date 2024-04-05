data = input(Please input collected Data here:)

# Dummy-Daten in JSON-Datei speichern
json_file_path = 'data.json'
with open(json_file_path, 'a') as file:
    json.dump(dummy_data, file, indent=2)

print(f'Daten wurden erfolgreich in "{json_file_path}" hinzugefügt.')