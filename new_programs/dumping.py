import json

numbers = [1,2,3,4,5,6,7,8]

file_name = "numbers.json"

with open(file_name, 'w') as f:

	json.dump(numbers, f)