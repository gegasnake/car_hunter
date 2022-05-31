"""
This module is responsible for creating tables in the database
"""
import sqlite3

connection_obj = sqlite3.connect('car_storage.db')

cursor_obj = connection_obj.cursor()

table = """ CREATE TABLE IF NOT EXISTS CARS (
            Car_Id INT PRIMARY KEY,
            Sent BOOLEAN NOT NULL,
            Url VARCHAR(255) NOT NULL,
            Price INT NOT NULL,
            Mileage INT NOT NULL,
        """

cursor_obj.execute(table)

connection_obj.commit()