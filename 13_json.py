import json
data = {'car':'bmw','age':'20','name':'mujjamil'}
data_1 = json.dumps(data)
data_2 = json.loads(data_1)

print(data_2['car'])