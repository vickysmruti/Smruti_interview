import json
dir = {"1": "a", "5": "e", "3": "c", "4": "d"}
json_obj = json.dumps(dir, sort_keys=True, indent=4)
print(json_obj)