from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/test.html")
def test():
    import json
    json_file_path = 'data.json'
    with open(json_file_path, 'r') as file:
        json_data = file.read()
    data = json.loads(json_data)
    return render_template("test.html", table_data=data) 
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    print("Website started")
    app.run(debug=True, host='192.168.50.33', port=80)
