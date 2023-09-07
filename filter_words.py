import json

with open('words_dictionary.json', 'r') as file:
    json_object = json.load(file)

output_dict = {x:'1' for x in json_object.keys() if (len(x) <= 6 and len(x) >= 3)}
output_json = json.dumps(output_dict)

with open('filtered_dictionary.json', 'w') as file:
    file.write(output_json)
