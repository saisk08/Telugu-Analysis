# To create user profiles and charts
import json
import sys
import _init_paths
from utils.python.basicinfo import basics
from utils.python.profile import create_profile, create_readme
from utils.python.plotter import make_bar_plot
from utils.python.create_index import create_index
import os
from tqdm import tqdm
from termcolor import colored

# Get the json data
ver1_file = open('ver1.json')
ver2_file = open('ver2.json')
ver1_data = json.load(ver1_file)
ver2_data = json.load(ver2_file)

# Create user profile for all user
print(colored('Generating pages...', 'blue'))
for user in tqdm(ver1_data):
    basic_info = basics(user, ver1_data[user])
    create_profile(basic_info, 1)
create_readme(ver1_data, 1)

for user in tqdm(ver2_data):
    basic_info = basics(user, ver2_data[user])
    create_profile(basic_info, 2)
create_readme(ver2_data, 2)
create_index(ver1_data, ver2_data)
print(colored('Pages generated', 'green'))
