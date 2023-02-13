import requests
import json
import time
import os

with open('mock_data/data.json', 'r') as f:
    data = '[' + f.read()[:-1] + ']'
    data = json.loads(data)

API_ENDPOINT = "http://{0}:8090/update_observations".format(os.getenv('middleware_ip', 'teleicu_middleware'))
# API_ENDPOINT = "http://127.0.0.1:8090/update_observations"

while True:
    for req_data in data:
        try:
            print (len(req_data), flush=True)
            r = requests.post(url=API_ENDPOINT, data=json.dumps(req_data))
            print("The response is: %s" % r.text)
        except Exception as e:
            print(e)
        time.sleep(4)
