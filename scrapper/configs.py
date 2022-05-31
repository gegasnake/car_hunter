# "TypeID=0&ForRent=0&Mans=3.98.1792.4634.1791.8337.99.1763.100.1793.101&CurrencyID=3&MileageType=1&Page=1"
# https://api2.myauto.ge/appdata/other_ka.json
from scrapper.constants import Currencies, VehicleType

cars_config = [
    {
        "TypeID": VehicleType.CAR.value,
        "ForRent": 0,
        "CurrencyID": Currencies.USD.value,
        "MileageType": 1,
        "PriceFrom": 900,
        "PriceTo": 10000,
        "Mans": {
            "car_name": "BMW",
            "car_id": 3,
            "models": [
                60, 61, 62, 63, 2226, 64, 65, 66, 67, 68, 69, 2230
            ]
        }
    },

]
