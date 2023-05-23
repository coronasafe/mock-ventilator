import json
import os

input_file = os.getenv("IN", "mock_data/data.json")
output_file = os.getenv("OUT", input_file)

with open(input_file, "r") as f:
    data = f.read()
    data = json.loads(data)


def update_device_id():
    """Adds 100 to the last octet of the IP address"""
    list_of_lists_of_lists = data[:]
    for list_of_lists in list_of_lists_of_lists:
        for list_of_dicts in list_of_lists:
            for dict_ in list_of_dicts:
                ip = dict_["device_id"]
                ip = ip.split(".")
                ip[-1] = str(int(ip[-1]) + 100)
                ip = ".".join(ip)
                dict_["device_id"] = ip

    with open(output_file, "w") as f:
        f.write(json.dumps(list_of_lists_of_lists, indent=4))


update_device_id()
