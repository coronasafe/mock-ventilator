import requests
import json
import time
import os
from datetime import datetime, timedelta

with open("mock_data/data.json", "r") as f:
    data = f.read()
    data = json.loads(data)

API_ENDPOINT = "https://{0}:8090/update_observations".format(
    os.getenv("middleware_ip", "teleicu_middleware")
)


# API_ENDPOINT = "http://127.0.0.1:8090/update_observations"

print(API_ENDPOINT)


def update_date_time(list_of_lists):
    # get current time in UTC
    now = datetime.utcnow()
    # add 5:30 hours to the current time
    now = now + timedelta(hours=5, minutes=30)
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Time =", current_time)
    for list_of_dicts in list_of_lists:
        for dict_ in list_of_dicts:
            dict_["date-time"] = current_time
    return list_of_lists


def mock_cns():
    list_of_lists_of_lists = data[:]
    for list_of_lists in list_of_lists_of_lists:
        list_of_lists = update_date_time(list_of_lists)
        try:
            r = requests.post(
                url=API_ENDPOINT,
                data=json.dumps(list_of_lists),
                headers={"Content-Type": "application/json"},
            )
            print("The response is: %s" % r)
        except Exception as e:
            print(e)
        time.sleep(4)


while True:
    mock_cns()
