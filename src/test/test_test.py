import requests
import json
import pytest


def test_areas():
    # get json with areas
    req = requests.get("https://api.hh.ru/areas")
    json_list = json.loads(req.text)

    # takes id's of areas from json and put in the list
    areas_id = [""]  # empty element in list also needed for requests testing
    for i in json_list:
        areas_id.append(i.get("id"))

    # positive scenarios
    for id_area in areas_id:
        req_areas = requests.get("https://api.hh.ru/areas/{}".format(id_area))
        assert req_areas.status_code == 200

    # negative scenarios
    invalid_list = ['9999999999999999', 'qwerty', '-1',
                    '<script>alert("wtf")</script>', ' ']  # TODO продумать классы эквивалентности
    for el in invalid_list:
        req_areas = requests.get("https://api.hh.ru/areas/{}".format(el))
        assert req_areas.status_code == 404 # TODO прописать или или или 400/403/404


# Запрос поиск  по компаниям с указанием региона поиска(Россия), по строке "IQ Орtiоn Sоftwаre"
def test_search():
    payload = {'text': 'IQ Орtiоn Sоftwаre', 'area': '113'}  # TODO values задавать из вне
    req = requests.get("https://api.hh.ru/employers", params=payload)
    assert req.status_code == 200


# Проверить наличие вакансии "QA Engineer" у компании "IQ Орtiоn Sоftwаre" в регионе "Санкт-Петербург"
# TODO ПРОТЕСТИТЬ !! Внимание: неизвестные параметры и параметры с ошибкой в названии игнорируются
def test_vacancy():
    payload = {'text': 'QA Engineer IQ Орtiоn Sоftwаre'}  # TODO values задавать из вне
    req = requests.get("https://api.hh.ru/vacancies", params=payload)
    assert req.status_code == 200