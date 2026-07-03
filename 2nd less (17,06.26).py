from operator import truediv, and_

# name = True
# name2 = False

# == -  сравнение двух значений
# != - 'не равно''

# print('helloo'> 'hello') - true
# print('helo'> 'hello') - false
# print('hello'>= 'hello') - true
# print ({} == []) - false

# результат сравнения -always bool
# сравнение разных типов данных - всегда  false , кроме числовых



# print(list((1,2,3))== [1,2,3]) - true

# n1 = [1,2,3]
# n2 = [1,2,3]
# print(n1 is n2) - false

# str1 = 'hello'
# оператор принадлежности  in
# print('ll' in str1) - true

# list1 = [12.33,5,6,7]
# print(2 in list1) - 2 есть в списке1 - false

# not in
# str1 = 'hello'
# print('ll' not in str1) - f
# print(not('ll' in str1)) - f


# and or not

# print(True and False) #true - коньюнкция
# 0 0 0
# 1 0 0
# 0 1 0
# 1 1 1

# print(True or False) -  хотя бы 1 истина - дизьюнкция
# 0 0 0
# 1 0 1
# 0 1 1
# 1 1 1

# not
# 0 -> 1
# 1 -> 0


# импликация -  ложь только если из истины ложь (1<=0) = 0
# <=
# A -> B
# 0 0 1
# 0 1 1
# 1 0 0
# 1 1 1
# a = True
# b = False
# print (a <= b) - false


# эквивалентность - <--> (1 если два одинак зннач) ==
# 0 0 1
# 1 0 0
# 0 1 0
# 1 1 1

# исключающее или ( 1 только если один истина - другой ложь , те 10 или 01)
# (+)
# ^
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 0
# a = True
# b = False
# print(a ^ b) - true
# print((a or b) and (a!=b))


# СТРЕЛКА ПИРСА (отрицание дизьюнкции(or), те 1 только если 00)
# print(not(a or b))
# 0 0 1
# 1 0 0
# 1 1 0
# 0 1 0


# ШТРИХ ШЕФФЕРА - ОТРИЦАНИЕ КОНЬЮНКЦИИ(AND) - те 1 если есть хотя бы один 0
# A/B
# not(a and b)
# 0 1 1
# 1 1 0
# 0 1 1
# 0 0 0

# ПОРЯДОК ДЕЙСТВИЙ
# алгебра логики
# 1 - ()
# 2 - not
# 3 - and(коньюнкц)
# 4 - or(дизьюнкц)
# 5 - A -> B (импликация)
# 6  - эквивалентность

# в python
# 1 - ()
# 2 - (**)
# 3 - (* / % //)
# 4 - (+-)
# 5 - ( >, <, >=,<=,!=)
# 6 - not
# 7 - and
# 8 - or


# A = '123A3A'
# int(строка, система счисления)
# print(int(A, 16))


# двоичное представление числа
# a = 20
# print(bin(a))

# o - для восьмеричной
# x -шестнадцатиричной
# b - двоичной

# print(format(20,'b'))
# print (f'{20:o}')


# восьмеричное предст числа
# oct
# print(oct(5))

# шестнадцатиричное
# print(hex(29))



import math #импорт название
# print(math.log10(100)) = 2
# print(math.sqrt(100)) = 2
# print(100**(1/2)) - получение корня

# округление
# a = 10.7
# print(int(a), a//1, math.floor(a)) - до меньшего

# до большего
# print(math.ceil(a))

# округление по мат правилам
# round(a)

# print(bool(1==1 and 0 <= 1))


# n1 = 10
# n2 = 15
# n3 = 17
# d1 =n1*(n3-n2)
# d2 = n2**2
# d3 = n3%3+d1
# d4 = d3//d2
# print(oct(d4))


a = '67'
b = '1B'
x= (- int(b, 16) + int(a, 8))/4
print(x)