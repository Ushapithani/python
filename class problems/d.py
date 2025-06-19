import json

data = {"name": "Usha", "age": 25, "city": "Amalapuram"}
json_string = json.dumps(data)

print(json_string)  # Output: '{"name": "Usha", "age": 25, "city": "Amalapuram"}'