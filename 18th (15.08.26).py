# !! list: изменяемый,индексируемый,нетипизированный
# append,extend,pop(0),clear,sort,remove(element),count,reverse,insert,index

# !! str - итерируемый , нетзиеняемый , индексируемый
# replace , split , lower, translate, find , join


# s = [1,2,3,4]
# print(sum(s))/min/max


#  !!!!! set: набор уникальных значений, неиндексируемый(как единое множество), итерируемый
# s = {1,2,3,'a',1,2,'a'}
# # for i in s:
# #     print(i)
# s.add(4)
# s.remove(2)
# s.discard(2) - удаляет элемент
# print(s)

# len , (not) in , add , remove , clear , copy, pop
# pop(удаляет первый элемент), при print возвращает удаленный элемент
# copy ( создает копию, с разной памятью)


# //
# s1 = {0,2,4,5,6,8}
# s2 = {0,1,3,5,7,9}

# s3 = s1.union(s2) #обьединение
# # s1.update(s2)
# s3 = s1 | s2
# print(s3)

# s3 = s1.intersection(s2) # пересечение
# s1.intersection_update(s3) # тож пересечение
# print(s1,s3)
# print(s1 & s2)


# s3 = s1.difference(s2) # выводит уникальные для s1 элементы, который нет в s2
# s1.difference_update(s2) # (изменяет сам обьект)
# print(s3,s1)
#
# s3 = s1.symmetric_difference(s2) # все за исключением пересечения, симметрическая разность
# s1.symmetric_difference_update(s2)
# s1 - s2
# print(s3)
# //


# #
# small_set = {3,5,7}
# big_set = {1,3,5,7,9}
#
# print(small_set.issubset(big_set)) # подмножество
# small_set <= big_set

# print(big_set.issuperset(small_set)) # надмножество


#
# Дан список fruits = ["яблоко", "банан", "яблоко", "апельсин", "банан", "киви"].
# Создайте из него множество уникальных фруктов и выведите количество уникальных элементов.

# fruits = ["яблоко", "банан", "яблоко", "апельсин", "банан", "киви"]
# a = set(fruits)
# print(a,len(a))


# s1 = {1,2,3}
# s2 = {4,5,6}
# print(s1.union(s2))
# print(s1|s2)


# a = {2,4}
# b = {1,2,3,4,5}
# print(a.issubset(b))
# print(a<=b)


# У вас есть три множества студентов, изучающих разные предметы:
# math_students = {"Анна","Борис","Вера","Глеб"}
# physics_students = {"Борис","Вера","Дмитрий","Елена"}
# chemistry_students = {"Вера","Глеб","Дмитрий","Жанна"}
# Найдите:
# Студентов, изучающих все три предмета
# Студентов, изучающих только математику
# Студентов, изучающих математику или физику, но не химию

# math_students = {"Анна","Борис","Вера","Глеб"}
# physics_students = {"Борис","Вера","Дмитрий","Елена"}
# chemistry_students = {"Вера","Глеб","Дмитрий","Жанна"}
#
# all3 = math_students & (physics_students & chemistry_students)
# print(all3)
#
# m = math_students.difference(physics_students | chemistry_students)
# print(m)
#
# m_or_ph = (math_students | physics_students) - (chemistry_students)
# print(m_or_ph)




# Даны два списка:
# list1 = [1, 3, 5, 7, 9, 11, 13, 15]
# list2 = [2, 3, 6, 7, 10, 11, 14, 15]
# Найдите:
# Элементы, которые есть в обоих списках
# Элементы, которые есть в первом списке, но отсутствуют во втором
# Элементы, которые есть только в одном из списков (симметричная разность)
#
# list1=[1,3,5,79,11,13,15]
# list2=[2,3,6,7,10,11,14,15]
# print(set(list1) & set(list2))
# print(set(list1) - set(list2))
# print(set(list1).symmetric_difference(set(list2)))

# У вас есть множество numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}. Напишите программу, которая:
# Удаляет все четные числа из множества, используя метод discard() в цикле.
# Добавляет квадраты всех оставшихся чисел.
# Выводит итоговое множество.
#
# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# for i in numbers.copy():
#     if i % 2 == 0:
#         numbers.discard(i)
#     else:
#         numbers.add(i**2)
# print(numbers)


