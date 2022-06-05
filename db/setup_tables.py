"""
This module is responsible for creating tables in the database
"""
import sqlite3

connection_obj = sqlite3.connect('car_storage.db')

cursor_obj = connection_obj.cursor()

table = """ CREATE TABLE IF NOT EXISTS CARS (
            car_id INT PRIMARY KEY,
            sent BOOLEAN NOT NULL,
            url VARCHAR(255) NOT NULL,
            price INT NOT NULL,
            mileage INT NOT NULL) 
        """

cursor_obj.execute(table)

connection_obj.commit()