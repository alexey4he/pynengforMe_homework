# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

user_Ipadress = input('Введите свой IP адрес сети в формате 10.1.1.0/24' + '\n')
'''
print('\n'+'Network:')

user_Ipadress = user_Ipadress.replace('/','.')
user_Ipadress = user_Ipadress.split('.')
digit_ip = [int(digit_ip) for digit_ip in user_Ipadress in digit_ip.isdigit()]

ip_address = digit_ip[:4]
ip1, ip2, ip3, ip4 = ip_address
mac_address = digit_ip[4:]


print(ip_address)
print(mac_address)

print('{:<8}   {:<8}   {:<8}   {:<8}'.format(ip1, ip2, ip3, ip4))
print('{:<08b}  {:<08b}  {:<08b}  {:<08b}'.format(ip1, ip2, ip3, ip4))
'''
