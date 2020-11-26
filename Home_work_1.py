# Сделать list из списка URL адресов (минимум 5).
# Написать цикл, который пробежит по списку и обратиться к каждому N раз (минимум 100)
# с помощью библиотеки requests.

import requests

sites_url = ['https://www.youtube.com', 'https://www.google.com', 'https://planner5d.com/ru']


def get_response(value):
    response = requests.get(value)
    print(response.text)
    print()
    print()
    print(response.status_code)


def many_requests(n, value):
    for i in range(n):
        get_response(value)
        i += 1


def my_func(n, sites_url):
    for i in sites_url:
        s = i
        many_requests(n, s)


my_func(2, sites_url)
