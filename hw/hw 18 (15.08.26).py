


# # 1. Создайте программу, которая анализирует текст:
# # Принимает две строки от пользователя.
# # Создает множества из букв каждой строки (без пробелов и знаков препинания).
# # Находит общие буквы, уникальные буквы первой строки, уникальные буквы второй строки.
# # Определяет, какая строка содержит больше уникальных букв.
# #1
# s1 = input()
# s2 = input()
# cls1 = []
# cls2 = []
# for i in s1:
#     if i.isalpha():
#         cls1.append(i)
# for i in s2:
#     if i.isalpha():
#         cls2.append(i)
# #2
# cls1 = set(cls1)
# cls2 = set(cls2)
# print('общие:', cls1 & cls2)
# print('уникальные буквы первой строки:', cls1 - cls2)
# print('уникальные буквы второй строки:', cls2 - cls1)
# #3
# if len(cls1) > len(cls2):
#     print('1st')
# elif len(cls2) == len(cls1):
#     print('equal')
# else:
#     print('2nd')






# 2. У вас есть три множества участников книжного клуба, читающих разные жанры книг:
# fantasy_readers = {"Игорь", "Катя", "Лев", "Марина"}
# detective_readers = {"Катя", "Лев", "Никита", "Ольга"}
# sci_fi_readers = {"Лев", "Марина", "Никита", "Павел"}
# Найдите:
# Участников, которые читают книги всех трёх жанров.
# Участников, которые читают только фантастику.
# # Участников, которые читают ровно два жанра
#
# fantasy_readers = {"Игорь", "Катя", "Лев", "Марина"}
# detective_readers = {"Катя", "Лев", "Никита", "Ольга"}
# sci_fi_readers = {"Лев", "Марина", "Никита", "Павел"}
# #1
# print(fantasy_readers & detective_readers & sci_fi_readers)
# #2
# print(fantasy_readers - detective_readers - sci_fi_readers)
#3
# all = fantasy_readers | detective_readers | sci_fi_readers
# for i in all:
#     c = 0
#     if i in fantasy_readers:
#         c += 1
#     if i in detective_readers:
#         c += 1
#     if i in sci_fi_readers:
#         c += 1
#     if c == 2:
#         print(i)



# 3.В школе есть три множества учеников, занимающихся разными видами спорта:
# football_players = {"Алексей", "Богдан", "Вика", "Дарья"}
# basketball_players = {"Богдан", "Вика", "Егор", "Зоя"}
# volleyball_players = {"Вика", "Дарья", "Егор", "Ирина"}
# Найдите:
# Всех учеников, которые занимаются хотя бы одним видом спорта.
# Учеников, которые занимаются ровно одним видом спорта.
# Учеников, которые занимаются волейболом, но не занимаются баскетболом.
#
# football_players = {"Алексей", "Богдан", "Вика", "Дарья"}
# basketball_players = {"Богдан", "Вика", "Егор", "Зоя"}
# volleyball_players = {"Вика", "Дарья", "Егор", "Ирина"}
# 1
# all = football_players | basketball_players | volleyball_players
# print(all)
# 2
# all_list = list(football_players)+list(basketball_players)+list(volleyball_players)
# only1 = []
# for player in all_list:
#     if all_list.count(player) == 1:
#         only1.append(player)
# print(set(only1))
# 3
# vol = volleyball_players - basketball_players
# print(vol)




# 4.В языковой школе есть три множества студентов, изучающих разные языки:
# english_students = {"Михаил", "Наташа", "Олег", "Полина"}
# spanish_students = {"Наташа", "Олег", "Роман", "Света"}
# french_students = {"Олег", "Полина", "Роман", "Татьяна"}
# Создайте множество всех студентов и добавьте нового студента "Антон" в группу английского языка.
# Найдите студентов, которые изучают только один язык, с помощью итерации по множествам.
# Удалите студента "Олег" из всех групп.
#
# english_students = {"Михаил", "Наташа", "Олег", "Полина"}
# spanish_students = {"Наташа", "Олег", "Роман", "Света"}
# french_students = {"Олег", "Полина", "Роман", "Татьяна"}
# #
# # 1
# english_students.add('Антон')
# all = english_students | spanish_students | french_students
# print(all)
# # 2
# only1 = set()
# for student in all:
#     c = 0
#     if student in english_students:
#         c += 1
#     if student in spanish_students:
#         c += 1
#     if student in french_students:
#         c += 1
#     if c == 1:
#         only1.add(student)
# print(only1)
# 3
# english_students.discard('Олег')
# spanish_students .discard('Олег')
# french_students .discard('Олег')

