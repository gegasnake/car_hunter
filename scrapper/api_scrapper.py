from pprint import pprint

import requests
import sqlite3
from db.car_crud import create_cars, get_existing_max_car_id

connection_obj = sqlite3.connect('db/car_storage.db')

cursor_obj = connection_obj.cursor()


def get_url(config, page=1):
    const_url = "https://api2.myauto.ge/ka/products?"
    # Car models
    model_list = config["Mans"]["models"]
    # inserting car id
    model_list.insert(0, config["Mans"]["car_id"])

    # joining a string to create an url
    mans_string = '.'.join(map(str, model_list))
    # print(mans_string)
    url_format = const_url + f"TypeID={config['TypeID']}&ForRent={config['ForRent']}&Mans={mans_string}&" \
                             f"CurrencyID={config['CurrencyID']}&" \
                             f"MileageType={config['MileageType']}&Page={page}"

    return url_format


def fetch_data(config):
    existing_max_id = get_existing_max_car_id()
    dictionary = {}
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"}
    api_url = get_url(config)
    # getting url with user agent
    response = requests.get(api_url, headers=headers)
    # This is a cycle, which runs down on cars and checks if car is new, it checks it with car_id-s
    for car_info in range(len(response.json()['data']['items'])):
        if cursor_obj.execute("SELECT id from CARS WHERE id=(SELECT MAX(id) from CARS)") < dictionary[response.json()['data']['items'][car_info]['car_id']]:
            create_cars(response, dictionary, car_info)
            connection_obj.commit()

        # It just keeps information in dictionary to track and to see information easily
        dictionary[response.json()['data']['items'][car_info]['car_id']] = response.json()['data']['items'][car_info]

    sorted_dictionary = sorted(dictionary.items())
    pprint(sorted_dictionary)
    return sorted_dictionary

