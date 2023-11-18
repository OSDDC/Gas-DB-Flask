from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Beispiel-Daten
sensor_data = [
    {"date": "22.01.2021", "ort": "Mannheim", "CO": 62, "NO2": 15, "C2H5OH": 47, "H2": 89, "NH3": 73, "CH4": 36, "C3H8": 50, "C4H10": 21, "LPG": 94, "GPL": 18, "UVA": 62, "UVB": 79},
    {"date": "22.01.2021", "ort": "Ludwigshafen", "CO": 53, "NO2": 84, "C2H5OH": 42, "H2": 17, "NH3": 91, "CH4": 68, "C3H8": 76, "C4H10": 59, "LPG": 83, "GPL": 5, "UVA": 32, "UVB": 45},
    {"date": "22.01.2021", "ort": "Weinheim", "CO": 83, "NO2": 76, "C2H5OH": 92, "H2": 28, "NH3": 41, "CH4": 12, "C3H8": 50, "C4H10": 61, "LPG": 35, "GPL": 79, "UVA": 7, "UVB": 90},
    {"date": "22.01.2021", "ort": "Heidelberg", "CO": 25, "NO2": 57, "C2H5OH": 80, "H2": 68, "NH3": 96, "CH4": 29, "C3H8": 48, "C4H10": 64, "LPG": 93, "GPL": 12, "UVA": 41, "UVB": 23}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_sensor_data')
def get_sensor_data():
    return jsonify(sensor_data)

if __name__ == '__main__':
    app.run(debug=True)
