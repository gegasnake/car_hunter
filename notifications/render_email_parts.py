"""Construct email parts such as subjects, recipients, message body"""
import logging

from db.car_crud import get_cars, update_car
from notifications.notifications import send_email_function
from typing import List


def render_subject() -> str:
    """render a subject of an email"""
    subject = "Cars you may be interested in:\n"
    return subject


def render_message(car_info: List[dict]) -> str:
    """ Render e-mail massage text"""
    logging.basicConfig(level=logging.INFO)
    log_number = 0
    string_of_urls = ""
    for car in car_info:
        if car['sent'] == 0:
            message = f"{car['url']}:{car['price']}\n"
            string_of_urls += message
            log_number += 1

        update_car(car['car_id'])

    logging.info(log_number)
    if log_number == 0:
        return "Nothing to show!"
    else:
        return string_of_urls


def send_whole_email():
    """This function takes no arguments and sends whole email message with
    subject and rendered message with help of other functions"""
    if render_message(get_cars()) == "Nothing to show!":
        pass
    else:
        send_email_function(render_subject(), render_message(get_cars()))

    return "Nothing!"





