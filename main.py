from scrapper.api_scrapper import fetch_data
from scrapper.configs import cars_config


def main():
    for car_config in cars_config:
        fetch_data(car_config)


if __name__ == '__main__':
    main()
