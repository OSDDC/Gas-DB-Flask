import json

# Dateinamen
input_filename = 'drone.json'
output_filename = 'data.json'

# Inhalte aus drone.json lesen
with open(input_filename, 'r', encoding='utf-8') as infile:
    drone_data = json.load(infile)

# Inhalte in eine Liste packen
data_to_write = [drone_data]

# Inhalte in data.json schreiben
with open(output_filename, 'w', encoding='utf-8') as outfile:
    json.dump(data_to_write, outfile, ensure_ascii=False, indent=4)

print(f"Die Daten aus {input_filename} wurden erfolgreich in {output_filename} geschrieben.")
