api_url = "https://api.hh.ru/"

success = [x+200 for x in range(100)]
client_error = [x+400 for x in range(100)]

invalid_list = ['9999999999999999', 'qwerty', '-1',
                 '<script>alert("wtf")</script>', ' '] # TODO продумать классы эквивалентности


payload_employers = {'text': 'IQ Орtiоn Sоftwаre', 'area': '113'}
payload_vacancies = {'text': 'QA Engineer IQ Орtiоn Sоftwаre'}
