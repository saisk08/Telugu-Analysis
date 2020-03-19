# To create user profiles and charts
import json
import sys
import _init_paths
from utils.python.basicinfo import basics

# Get the json data
json_file = open('data.json')
data = json.load(json_file)
# create user profile for each key
for user in data:
    basic_info = basics(data[user])
    print(basic_info)
# plot bar graph
