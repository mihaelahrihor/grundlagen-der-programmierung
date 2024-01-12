import json

# x = '{"name":"Andrei", "age":20}'
#
# y = json.loads(x)
#
# print(y['age'])

x = {
  "name": "Andrei",
  "age": 20,
  "married": True,
  "divorced": False,
  "children": ("Ana","Marian"),
  "pets": None,
  "cars": [
    {"model": "BMW M5", "mpg": 27.5},
    {"model": "Ford Focus", "mpg": 24.1}
  ]
}

print(json.dumps(x))