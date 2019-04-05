# Python 3.XX

import requests
import json
from test_data import *
from threading import Thread

response = requests.get(api_url + "areas")
json_list = json.loads(response.text)
areas_id = [""]  # empty element in list also needed for requests testing


# takes id's of areas from json and put in the list
def parse_id():
    def parse_areas(areas):
        for area in areas.get("areas"):
            areas_id.append(area.get("id"))
            parse_areas(area)

    for top_level_area in json_list:
        areas_id.append(top_level_area.get("id"))
        parse_areas(top_level_area)


def run_in_thread(fn):
    def run(*k, **kw):
        t = Thread(target=fn, args=k, kwargs=kw)
        t.start()
        return t

    return run


@run_in_thread
def send_request(l, p):
    for id_area in l:
        response = requests.get(api_url + "areas" + "/{}".format(id_area))
        print("In thread: " + p)
        assert response.status_code in success


parse_id()

l_1 = [x for x in range(5)]
l_2 = [x + 100 for x in range(5)]

thread1 = send_request(l_1, "1")
thread2 = send_request(l_2, "2")
thread1.join()
thread2.join()

# thread1.join()
# thread2.join()
