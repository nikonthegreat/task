# Python 3.XX

import requests
import json
from test_data import *
from threading import Thread


def test_areas():
    """
    Function tests get method of https://api.hh.ru/areas.
    """
    # get json with areas
    response = requests.get(api_url+"areas")
    json_list = json.loads(response.text)
    areas_id = [""]  # empty element in list also needed for requests testing
    body_list = []
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
            body_list.append(response.text)
            assert response.status_code in success

    parse_id()

#   l_1 = [x for x in areas_id if areas_id.index(x) % 7 is 0]
#   l_2 = [x for x in areas_id if areas_id.index(x) % 7 is 1]
#   l_3 = [x for x in areas_id if areas_id.index(x) % 7 is 2]
#   l_4 = [x for x in areas_id if areas_id.index(x) % 7 is 3]
#   l_5 = [x for x in areas_id if areas_id.index(x) % 7 is 4]
#   l_6 = [x for x in areas_id if areas_id.index(x) % 7 is 5]
#   l_7 = [x for x in areas_id if areas_id.index(x) % 7 is 6]
#   l_8 = [x for x in areas_id if areas_id.index(x) % 7 is 7]

    for el in range(16):
        locals()["thread_list"+str(el)] = [x for x in areas_id if areas_id.index(x) % 8 is el]

    for el in range(16):
        locals()["thread" + str(el)] = send_request(locals()["thread_list"+str(el)], "{}".format(el))

    for el in range(16):
        locals()["thread" + str(el)].join()
    print("Длинааааааааааа"+str(len(body_list)))
#   thread1 = send_request(l_1, "1")
#   thread2 = send_request(l_2, "2")
#   thread3 = send_request(l_3, "3")
#   thread4 = send_request(l_4, "4")
#   thread5 = send_request(l_5, "5")
#   thread6 = send_request(l_6, "6")
#   thread7 = send_request(l_7, "7")
#   thread8 = send_request(l_8, "8")
#   thread1.join()
#   thread2.join()
#   thread3.join()
#   thread4.join()
#   thread5.join()
#   thread6.join()
#   thread7.join()
#   thread8.join()

    # negative scenarios
    for el in invalid_list:  # from test_data module
        response = requests.get(api_url+"areas"+"/{}".format(el))
        assert response.status_code in client_error

    # negative scenarios
    for el in invalid_list:  # from test_data module
        response = requests.get(api_url+"areas"+"/{}".format(el))
        assert response.status_code in client_error


# Запрос поиск  по компаниям с указанием региона поиска(Россия), по строке "IQ Орtiоn Sоftwаre"
def test_employers():
    """
    Function tests get method of https://api.hh.ru/employers.
    """
    payload = payload_employers  # from test_data module
    response = requests.get(api_url+"employers", params=payload)
    assert response.status_code in success


# Проверить наличие вакансии "QA Engineer" у компании "IQ Орtiоn Sоftwаre" в регионе "Санкт-Петербург"
# TODO ПРОТЕСТИТЬ !! Внимание: неизвестные параметры и параметры с ошибкой в названии игнорируются
def test_vacancy():
    """
    Function tests get method of https://api.hh.ru/vacancies.
    """
    payload = payload_vacancies  # from test_data module
    response = requests.get(api_url+"vacancies", params=payload)
    assert response.status_code in success