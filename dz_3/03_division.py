# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37

# TODO здесь ваш код

educational_grant, expenses, еducational_g = 10000, 12000, 0
i = 1
while i < 11:
    еducational_g += expenses - educational_grant
    expenses = expenses * 1.03
    i += 1
print (еducational_g)