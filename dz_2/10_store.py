#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа'] # код лампы 12345
lamps_item = store[lamp_code][0] # айтем указывает на кол-во и цену ламп, через код 12345
lamps_quantity = lamps_item['quantity'] # указывает только количество ламп
lamps_price = lamps_item['price'] # указывает только цену ламп
lamps_cost = lamps_quantity * lamps_price # умножает количество на цену
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
Стол
stol_code=goods['Стол']
stol_item1=store[stol_code][0]
stol_item2=store[stol_code][1]
stol_quantity=stol_item1['quantity']+stol_item2['quantity']
stol_price=stol_item1['price']+stol_item2['price']
stol_cost=stol_price*stol_quantity
stol='Стол -', stol_quantity, 'шт, стоимость', stol_cost, 'руб'
print(stol)
или
stol_cost1 = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
stol_cost2 = store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
stol_cost3 = stol_cost1+stol_cost2

Диван
divan_code=goods['Диван']
divan_item1=store[divan_code][0]
divan_item2=store[divan_code][1]
divan_quantity=divan_item1['quantity']+divan_item2['quantity']
divan_price=divan_item1['price']+divan_item2['price']
divan_coast=divan_quantity*divan_price
divan=('Диван -', divan_quantity, 'шт, стоимость', divan_cost, 'руб')
print(divan)
или
divan_cost1=store[goods['Диван']][0]['quantity']*store[goods['Диван']][0]['quantity']
divan_cost2=store[goods['Диван']][1]['quantity']*store[goods['Диван']][1]['quantity']
divan_cost3=divan_cost1+divan_cost2


Стул
stul_code=goods['Стул']
stul_item0=store[stul_code][0]
stul_item1=store[stul_code][1]
stul_item2=store[stul_code][2]
stul_quantity=stul_item0['quantity']+stul_item1['quantity']+stul_item2['quantity']
stul_price=stul_item0['price']+stul_item1['price']+stul_item2['price']
stul_cost=stul_quantity*stul_price
stul=('Стул -', stul_quantity, 'шт, стоимость', stul_cost, 'руб')
print(stul)
или
stul_cost1=store[goods['Стул']][0]['quantity']*store[goods['Стул']][0]['price']
stul_cost2=store[goods['Стул']][1]['quantity']*store[goods['Стул']][1]['price']
stul_cost3=store[goods['Стул']][2]['quantity']*store[goods['Стул']][2]['price']
stul_cost=stul_cost1+stul_cost2+stul_cost3
stul_quantity=store[goods['Стул']][0]['quantity']
stul_quantity1=store[goods['Стул']][1]['quantity']
stul_quantity2=store[goods['Стул']][2]['quantity']
stul_quantity33=stul_quantity+stul_quantity1+stul_quantity2
stul=('Стульчик -', stul_quantity33, 'шт, стоимость', stul_cost, 'руб')
print(stul)
('Стульчик -', 153, 'шт, стоимость', 10311, 'руб')

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






