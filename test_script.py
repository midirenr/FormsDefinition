import requests
import sys

try:
    response = requests.get('http://127.0.0.1:8000/get_form/')
except requests.exceptions.ConnectionError:
    print('Не удается отправить запрос! Пожалуйста запустите сервер Django командой: "python manage.py runserver" в '
          'корне проекта')
    sys.exit()

test_1_url = 'http://127.0.0.1:8000/get_form/?phone=+79250721259&email=genshmidir@gmail.com'
test_2_url = 'http://127.0.0.1:8000/get_form/?phone=+79250721259&email=genshmidir@gmail.com&birthday=01.01.2000'
test_3_url = 'http://127.0.0.1:8000/get_form/?phone=+79250721259&email=genshmidirgmail.com'

test_1_response = requests.get(test_1_url)
test_2_response = requests.get(test_2_url)
test_3_response = requests.get(test_3_url)

test_1_expect = b'registration_1'
test_2_expect = b'registration_2'
test_3_expect = b'{"phone": "phone", "email": "text"}'

print(f"Тест №1: \n"
      f"URL: {test_1_url}\n"
      f"Ожидали получить: {test_1_expect}\n"
      f"Получили: {test_1_response.content}\n"
      f"Успех: {test_1_expect == test_1_response.content}\n")


print(f"Тест №2: \n"
      f"URL: {test_2_url}\n"
      f"Ожидали получить: {test_2_expect}\n"
      f"Получили: {test_2_response.content}\n"
      f"Успех: {test_2_expect == test_2_response.content}\n")

print(f"Тест №3: \n"
      f"URL: {test_3_url}\n"
      f"Ожидали получить: {test_3_expect}\n"
      f"Получили: {test_3_response.content}\n"
      f"Успех: {test_3_expect == test_3_response.content}\n")


