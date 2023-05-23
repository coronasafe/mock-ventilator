import json
import os

input_file = os.getenv("IN", "mock_data/data.json")
output_file = os.getenv("OUT", input_file)

with open(input_file, "r") as f:
    data = f.read()
    data = json.loads(data)

source_map = {
    "heart-rate": {
        "observation_id": "PEEP",
        "unit": "cmH2O",
        "low-limit": "0",
        "high-limit": "15",
    },
    "spo2": {
        "observation_id": "FiO2",
    },
    "respiratory-rate": {
        "observation_id": "R.Rate",
    },
    "pulse-rate": {
        "observation_id": "Insp-Time",
        "unit": "sec",
        "low-limit": "0",
        "high-limit": "5",
    },
    "waveform": {
        "II": "P",
        "Pleth": "F",
        "Respiration": "V",
    },
}


def transform_data():
    waveform_source_map = source_map.pop("waveform")

    list_of_lists_of_lists = data[:]
    for list_of_lists in list_of_lists_of_lists:
        for list_of_dicts in list_of_lists:
            for dict_ in list_of_dicts:
                map_ = source_map.get(dict_["observation_id"])
                if dict_["observation_id"] == "waveform":
                    dict_["wave-name"] = waveform_source_map[dict_["wave-name"]]
                    continue
                if not map_:
                    list_of_dicts.remove(dict_)
                    continue
                for key, value in map_.items():
                    dict_[key] = value

    with open(output_file, "w") as f:
        f.write(json.dumps(list_of_lists_of_lists, indent=4))


transform_data()
