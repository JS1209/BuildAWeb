# This file is for every utility functions. They are less focussed on one specific thing than for example managers.py or
# writers.py. These functions can be called anywhere any time at any level, whereas writers will only be called by managers.
import json
import datetime

# We want a tripple nested json object. First we initialize the object by "just writing" a json string in a .json file.
# Then we fill the object with some basic things that we know there are for sure, like (if) a login system (is enabled) and
# it's extra attributes like NUM, DOB and NAT. By initializing, they are all turned off.

def initialize_properties(properties, user_name):
  with open(properties, 'w') as f:
    f.write('{}')
    print("Properties created")
  
  date = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

  json_add_pair_top(properties, "Name", "%s" %user_name)
  json_add_pair_top(properties, "Datetime", "%s" %date)
  json_add_pair_top(properties, "Systems", {})
  json_add_pair_middle(properties, "Systems", "Login", {})
  json_add_pair_bottom(properties, "Systems", "Login", "Enabled", "0")
  json_add_pair_bottom(properties, "Systems", "Login", "DOB", "0")
  json_add_pair_bottom(properties,"Systems", "Login", "NUM", "0")
  json_add_pair_bottom(properties, "Systems", "Login", "NAT", "0")

# Each of the following functions can change a pair nested deeper in the object. They work exactly the same. Three levels, hence top,
# middle and bottom. To access a key-value pair, first open the file (json.load(file) handles the key lookup functionality), then
# simply use the key as index to look up some value. For instance data["Systems"]["Login"]["Enabled"] returns "0" (after initializing.)
def json_add_pair_top(file, key, value):
  with open(file) as json_file:
    data = json.load(json_file)
    data[key] = value
    with open(file, 'w') as json_file:
      json.dump(data, json_file, indent=2)

def json_add_pair_middle(file, prop, key, value):
  with open(file) as json_file:
    data = json.load(json_file)
    data[prop][key] = value
    with open(file, 'w') as json_file:
      json.dump(data, json_file, indent=2)

def json_add_pair_bottom(file, prop, att, key, value):
  with open(file) as json_file:
    data = json.load(json_file)
    data[prop][att][key] = value
    with open(file, 'w') as json_file:
      json.dump(data, json_file, indent=2)

# The next functions update the properties.json, for enabling the login system for example, or switching the NUM or DOB attributes. Since
# we only work with 0's and 1's, we only need the key, and set its value to the opposite of what it is. I named it json_update_switch because
# I don't know if we need key value(STRING) pairs in the future. If we do, those functions will simply be called json_update.
def json_update_switch_top(file, key):
  with open(file) as json_file:
    data = json.load(json_file)

    # We need to switch between 1 and 0, respectively True and False. We cannot simple do "data[key] = not data[key]", because 1 and 0 don't
    # have a negation. Therefore, we do abs(data[key] - 1); if the value goes from 0 to -1, it gets absoluted to 1
    data[key] = abs(int(data[key]) - 1)
    with open(file, 'w') as json_file:
      json.dump(data, json_file)

def json_update_switch_middle(file, prop, key):
  with open(file) as json_file:
    data = json.load(json_file)
    data[prop][key] = abs(int(data[prop][key]) - 1)
    with open(file, 'w') as json_file:
      json.dump(data, json_file)

def json_update_switch_bottom(file, prop, att, key):
  with open(file) as json_file:
    data = json.load(json_file)
    data[prop][att][key] = abs(int(data[prop][att][key]) - 1)
    with open(file, 'w') as json_file:
      json.dump(data, json_file)

# Returns the values at certain keys at different levels
def json_value_by_key_top(file, key):
  with open(file) as jsonFile:
    data = json.load(jsonFile)
    return(data[key])

def json_value_by_key_middle(file, prop, key):
  with open(file) as jsonFile:
    data = json.load(jsonFile)
    return(data[prop][key])

def json_value_by_key_bottom(file, prop, att, key):
  with open(file) as jsonFile:
    data = json.load(jsonFile)
    return(data[prop][att][key])