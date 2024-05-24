const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

app.use(cors());
app.use(bodyParser.json());

// Datenbankverbindung einrichten
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password', // Ersetze durch dein MySQL-Passwort
  database: 'sensor_data_db'
});

connection.connect(err => {
  if (err) {
    console.error('Error connecting to the database:', err);
    return;
  }
  console.log('Connected to the database');
});

// API-Endpunkt zum Abrufen der Daten
app.get('/data', (req, res) => {
  connection.query('SELECT * FROM sensor_data', (err, results) => {
    if (err) {
      return res.status(500).json({ error: err });
    }
    res.json(results);
  });
});

// API-Endpunkt zum Hinzufügen von Daten
app.post('/data', (req, res) => {
  const { LPG, Temp, Hum, Datum } = req.body;
  const query = 'INSERT INTO sensor_data (LPG, Temp, Hum, Datum) VALUES (?, ?, ?, ?)';
  connection.query(query, [LPG, Temp, Hum, Datum], (err, results) => {
    if (err) {
      return res.status(500).json({ error: err });
    }
    res.json({ success: true, id: results.insertId });
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
    