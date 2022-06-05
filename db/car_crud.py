"""
CRUD operations for car table
"""
import sqlite3
from scrapper.configs import cars_config
connection_obj = sqlite3.connect('db/car_storage.db')

cursor_obj = connection_obj.cursor()


def get_existing_max_car_id():
    find_max_id = "SELECT * FROM CARS WHERE Car_id = (SELECT MAX(Car_id) FROM CARS)"
    getting_max_car_command = cursor_obj.execute(find_max_id)
    return getting_max_car_command


def create_cars(response, data, car_info):
    creation = f"INSERT INTO CARS (car_id, sent, url, price, mileage) VALUES " \
               f"({data[response.json()['data']['items'][car_info]['car_id']]}," \
               f" False, myauto.ge/ka/{data[response.json()['data']['items'][car_info]['car_id']]}, " \
               f"{data[response.json()['data']['items'][car_info]['car_id']['price']]}, {cars_config['mileageType']} "
    creation_command = cursor_obj.execute(creation)
    connection_obj.commit()
    return creation_command


def get_cars():
    select_all = "SELECT * FROM CARS"
    cars = cursor_obj.execute(select_all)
    return cars


def get_car(car_id: int):
    selection = f"SELECT * FROM CARS WHERE car_id = {car_id}"
    car = cursor_obj.execute(selection)
    return car


def update_car(car_id: int):
    pass


def delete_car(car_id: int):
    pass
