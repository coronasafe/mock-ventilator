import requests
import json
import time
import os

with open('mock_data/data.json', 'r') as f:
    data = '[' + f.read()[:-1] + ']'
    data = json.loads(data)

API_ENDPOINT = "http://{0}:8090/update_observations".format(os.getenv('middleware_ip', 'teleicu_middleware'))
# API_ENDPOINT = "http://127.0.0.1:8090/update_observations"

list_of_lists_of_lists = data[:]
for list_of_lists in list_of_lists_of_lists:
    for list_of_dicts in list_of_lists:
        for dict_ in list_of_dicts:
            # get current time in the format '2023-02-20 18:05:32'
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            dict_['date-time'] = current_time

data = list_of_lists_of_lists[:]
while True:
    for req_data in data:
        try:
            print(len(req_data), flush=True)
            r = requests.post(url=API_ENDPOINT, data=json.dumps(req_data), headers={'Content-Type': 'application/json'})
            print("The response is: %s" % r.text)
        except Exception as e:
            print(e)
        time.sleep(4)
