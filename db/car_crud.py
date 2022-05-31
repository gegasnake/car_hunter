"""
CRUD operations for car table
"""
import sqlite3
from scrapper.configs import cars_config
connection_obj = sqlite3.connect('car_storage.db')

cursor_obj = connection_obj.cursor()


def create_cars(data):
    creation = f"INSERT INTO CARS (Car_Id, Sent, Url, Price, Mileage) VALUES ({car_id}," \
               f" False, myauto.ge/ka/{car_id}, {cars_config['Price']}, {cars_config['MileageType']} "
    command = cursor_obj.execute(creation)
    return command


def get_cars():
    select_all = "SELECT * FROM CARS"
    cars = cursor_obj.execute(select_all)
    return cars


def get_car(car_id: int):
    selection = f"SELECT * FROM CARS WHERE Car_id = {car_id}"
    car = cursor_obj.execute(selection)
    return car


def update_car(car_id: int):
    pass


def delete_car(car_id: int):
    pass
