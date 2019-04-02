import requests
import unittest
import json
from random import choice
import pprint

def get_areas(area_id):
    return requests.get("https://api.hh.ru/areas/{:d}".format(area_id))

# Тут я хочу получить id доступных тран
r = requests.get("https://api.hh.ru/areas")
json_areas_dict = r.json()

#for id in json_areas_dict:

print(json_areas_dict.keys())





DEFAULT_HEADER = 'application/json'

SUCCESS = 200
INCORRECT_HEADER = 400
ADDED = 201