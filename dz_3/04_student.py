# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

# TODO здесь ваш код

educational_grant, expenses, еducational_g = 10000, 12000, 0
i = 1
while i < 11:
    еducational_g += expenses - educational_grant
    expenses = expenses * 1.03
    i += 1
s3=('Студенту нужно попросить ')+str(round(еducational_g, 2)) +(' рублей')
print(s3)
