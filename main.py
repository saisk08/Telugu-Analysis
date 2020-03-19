# To create user profiles and charts
import json
import sys
import _init_paths
from utils.python.basicinfo import basics
from utils.python.profile import create_profile
import os

try:
    os.mkdir('Profiles')
except FileExistsError:
    pass

# Get the json data
json_file = open('data.json')
data = json.load(json_file)
# create user profile for each key
for user in data:
    basic_info = basics(data[user])
    create_profile(basic_info)

# plot bar graph
