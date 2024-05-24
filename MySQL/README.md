# Sensor Data Visualization

This project provides a simple web application to visualize sensor data stored in a MySQL database. It consists of a backend server built with Node.js and Express, a MySQL database to store sensor data, and a frontend interface using HTML and Chart.js for data visualization.

## Installation

## 1. MySQL Server Installation

#### Linux (Ubuntu):
```
sudo apt update
```
```
sudo apt install mysql-server
```

#### Windows:
- Download and install MySQL from [official website](https://dev.mysql.com/downloads/installer/).

#### macOS:
- Install using Homebrew:
```
brew update
```
```
brew install mysql
```
```
brew services start mysql
```

## 2. Create MySQL Database and Table

1. Log in to MySQL:
```
mysql -u root -p
```

2. Create a new database:
```
CREATE DATABASE sensor_data_db;
```

3. Use the new database:
```
USE sensor_data_db;
```

4. Create the table `sensor_data`:
```
CREATE TABLE sensor_data (
id INT AUTO_INCREMENT PRIMARY KEY,
LPG FLOAT,
Temp FLOAT,
Hum FLOAT,
Datum DATETIME
);
```

## 3. Install Node.js and npm

#### Linux/MacOS:
```
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
```
```
sudo apt-get install -y nodejs
```

#### Windows:
- Download and install Node.js from [official website](https://nodejs.org/en/download/).

## 4. Project Setup

1. Create a new directory for your project and navigate into it:
```
mkdir sensor_data_project
```
```
cd sensor_data_project
```


2. Initialize a new Node.js project:
```
npm init -y
```

3. Install required packages:
```
npm install express mysql2 cors body-parser
```

## 5. Backend Setup

1. Create a file named `server.js` in the project directory:
```
touch server.js
```


2. Copy and paste the code into `server.js`.

## 6. Frontend Setup

1. Create a file named `index.html` in the project directory:
```
touch index.html
```


2. Copy and paste the code into `index.html`.


## 7. Start the Server

1. Start the Node.js server:
```
node server.js
```


2. Open `index.html` in a browser to view the web interface and add data.

## Usage

- Access the web interface at http://localhost:3000/ in your browser.
- Enter the correct password to unlock the form for adding data.
- Add sensor data (LPG, Temp, Hum, Datum) using the form.
- The chart will dynamically update with the newly added data.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the GPL License. See the LICENSE file for details.
