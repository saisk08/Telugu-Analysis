# To create user profiles and charts
import json
import sys
import _init_paths
from utils.python.basicinfo import basics
from utils.python.profile import create_profile, create_readme
from utils.python.plotter import make_bar_plot
import os
from tqdm import tqdm
from termcolor import colored

try:
    os.mkdir('Profiles')
except FileExistsError:
    pass

# Get the json data
json_file = open('data.json')
data = json.load(json_file)

# Create user profile for each key
print(colored('Creating profiles...', 'blue'))
for user in tqdm(data):
    basic_info = basics(user, data[user])
    create_profile(basic_info)
create_readme(data)
print(colored('Profiles created', 'green'))

# # plot bar graph
# print(colored('Creating bar plots...', 'blue'))
# make_bar_plot(data)
# print(colored('Bar plots created', 'green'))
