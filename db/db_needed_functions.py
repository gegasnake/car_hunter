from db.db_connection import cursor_obj


def get_existing_max_car_id():
    find_max_id = "SELECT car_id FROM CARS WHERE car_id = (SELECT MAX(car_id) FROM CARS)"
    get_max_id_command = cursor_obj.execute(find_max_id)
    return cursor_to_dict(get_max_id_command)[0]  # zero because it fetches only one and there is no need for list.


def count_rows():
    count = "SELECT count(*) FROM CARS"
    count_command = cursor_obj.execute(count)
    return count_command


def cursor_to_dict(cursor):
    """converts cursor type to dictionary."""
    column_dictionaries_lst = []
    car_tuples = cursor.fetchall()
    index = 0
    for car_tuple in car_tuples:
        dct = {}
        for column in cursor.description:
            dct[column[0]] = car_tuple[index]
            index += 1

        column_dictionaries_lst.append(dct)
        index = 0

    print(column_dictionaries_lst)
    return column_dictionaries_lst
