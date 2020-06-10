# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

# TODO здесь ваш код
if (month == 1)
    print (31)
elif (month == 2)
print (28) ... ...
elif (month==12)
print (30)
else print (‘введен некорректный номер месяца’)
mkcrysman: И все
mkcrysman: Только ифами на каждый месяц
mkcrysman: Нельзя завязать на четность нечетность
mkcrysman: И я не уверен, что == это сравнение в питоне)) уточни))
mkcrysman: Вот так if month==1:
mkcrysman: Вот такая конструкция
mkcrysman: А не скобки
StrateX: == это равно
StrateX: сравнение да
StrateX: типо 1 == 1
StrateX: True
StrateX: 1 == 2
StrateX: False
StrateX: 1 != 2
mkcrysman: Вот топтал этот питон “if a>b :” что за конструкция дерьма такая))
StrateX: True
mkcrysman: If (a>b) {…}
mkcrysman: Вот это человеческая))
mkcrysman: Ато пробелы отступы