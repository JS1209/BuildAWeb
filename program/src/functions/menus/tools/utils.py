import json

def initialize_properties(properties, user_name):
  with open(properties, 'w') as f:
    f.write('[{"NAME":"%s"}]' %user_name)
    print("Properties created")

  add_json(properties, "NAME", user_name)
  add_json(properties, "Login", "0")
  add_json(properties, "NAT", "0")
  add_json(properties, "DOB", "0")

def update_tasks(user_name, line):
  with open('../../builtSites/' + user_name + '/tasks.txt', 'a') as file:
    file.write(line)
    return 0

def json_value_by_key(file, key):
  with open(file) as jsonFile:
    data = json.load(jsonFile)
    return(data[key])
    
def add_json(file, key, value):
  with open(file) as json_file:
    data = json.load(json_file)
    data[key] = value
    with open(file, 'w') as json_file:
      json.dump(data, json_file)
