# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
command1 = command1.split()
for vlans1 in command1:
    vlans1 = set(command1[-1].split(','))

command2 = command2.split()
for vlans2 in command2:
    vlans2 = set(command2[-1].split(','))

commonlistVlan = list(vlans1 & vlans2)
vlan = [int(vlan) for vlan in commonlistVlan if vlan.isdigit()]

vlan.sort()
print(vlan)
