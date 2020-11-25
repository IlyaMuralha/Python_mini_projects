import requests

# response = requests.get('https://google.com')
# print(response.text)
# print()
# print()
# print(response.status_code) # если вернулось 200 код выполнен успешно


alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'

# '10'-> '16'  0123456789abcdef
# 0 -> 0
# 9 -> 9
# 10 -> a
# 11 -> b
# 15 -> f
# 16 -> 10
# 17 -> 11

i = 0


while true:
    # i 10 -> 16
