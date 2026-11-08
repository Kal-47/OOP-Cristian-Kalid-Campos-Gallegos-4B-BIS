CREATE DATABASE IF NOT EXISTS login_system_db;
USE login_system_db;

CREATE TABLE IF NOT EXISTS users (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    passw VARCHAR(50) NOT NULL,
    usr_name VARCHAR(100) NOT NULL
);

INSERT INTO users (username, passw, usr_name) VALUES ('admin', '123', 'Overseer');

CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
);

INSERT INTO productos (nombre,precio,stock) VALUES
    ('The Fragile', 500, 5),
    ('Like Clockwork...,', 300, 3),
    ('Psycience Fiction', 200, 1);
