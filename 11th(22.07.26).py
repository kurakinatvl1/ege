# нетщиенямость,
# методы строк,
# len()
# in()
# min()/max()
# sum()
#
# st = 'hello world'
# print(len(st),st.__len__())

# st = 'hello world'
# print(st.index('w',2,9))#возвраш индекс первого вхождения элемента

# + - конкатанация
# world = 'world'
# hello = 'hello'
# print(hello+world)


# st = 'hello world'
# print(st.capitalize())
# print(st.title())

# методы регистра
# print(st.upper()) - все символы большие
# print(st.lower()) - все маленькие

# методы поиска
# print(st.endswith('world',0,8)) - чем заканч
# print(st.startswith('hello'0,8)) - ем начинается
# print(st.index('w',2,9))#возвраш индекс первого вхождения элемента
# print(st.find('hello',0,8)) - озвращ -1 если элемента нет

# s = 'seeafsga'
# letter = 'j'
# a =s.find(letter)
# if a != -1:
#  print(a)

# методы проверки символов
# s = '1234'
# print(s.isdigit()) - строка это число?
# print(s.isalnum())  # это буквы и цифры?
# print(s.isalpha()) - это буквы?
# print(s.isnumeric()) - более обшее чем digit

# print(st.islower())
# print(st.isupper())


# split
# s = 'hello world hello'
# print(s.split()) - разделение по пробельному символу
# print(s.split('w',1))   -# по какому символу и сколько раз делить
# print(s.rsplit('w',1))      - right split

# join
# ns = s.rsplit('w')
# print(', '.join(ns))


# удаление или замена
# st = '****hello world whello****'
# print(st.strip('*'))
# print(st.lstrip('*'))
# print(st.rstrip('*'))

# print(st.replace('hello', 'world',1))     - замена что б на что заменяетсябколво раз


# s = input()
# for i in s:
#     if i.isdigit() :
#         print('yes')
#         break
# else:
#     print('no')



# s = 'hello world'
# a = s.split()
# b =   ','.join(s)
# print(b)


# s = input()
# a = 'aeiouAEIOU'
# for i in a:
#     s =s.replace(i,'')
# print(s)


# s = input()
# d = 0
# for i in s:
#     if i.isdigit:
#        d += i
# print(d)


# #
# s = input()
# n = 0
#
# for i in s:
#     if i.isdigit():
#         n+=1
#         break
# if n >= 1:
#     print(s.upper())
# elif ' ' in s:
#     print(s.replace(' ', '*'))
# else:
#     print(s)



