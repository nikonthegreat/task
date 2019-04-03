import requests
import json

payload = {'text': 'IQ Орtiоn Sоftwаre', 'area': '113'} #TODO values задавать из вне
req = requests.get("https://api.hh.ru/employers", params=payload)
print(req.text)