# !!!!function
#
# def func(name,name1,name2):
#     print("funk 1",name,name1,name2)
# func('a','b','c')
# func('d','e','f')



# a = len
# print(a([]))

# # znachenie po umolch always in the end
# def func(age=19,name= 'user'):
#     print("hi",age,name)
# # func(name = 'boris')
# func(10,'ivan')


#
# def summ(x,y):
#     return x+y
# a = summ(10,20)
# print(a)


# def func(x,items=None):
#     if items == None:
#         items = []
#     items.append(x)
#
#     return items
# a = func(10)
# a1 = func(20)
# print(a,a1)

# def f(n):
#     n.append(4)
#
# my_list=[1,2,3]
# f(my_list)
# print(my_list)




# def f(n): - wont work
#     n+=100
# n1 = 10
# f(n1)
# print(n1)





# d = 10
# def f():
#     # local oblast vidimosti
#     global d
#     d = 20
#
#     a = 10
#     def g():
#         nonlocal a
#         a = 20
#         # ohvatuvausya(nonlokal) obl vidimosti,otnositelno drugoi funkcii
#     g()
#     print(a)
# f()
# print(d)







#
# Напишите функцию count_vowels(text, with_y=False),
# которая принимает строку и возвращает количество гласных латинских
# букв в ней (регистр не важен). Если второй аргумент равен True, буква "y"
# тоже считается гласной.
# Примеры вызова:
#
# count_vowels('Beautiful day') -> 6
# count_vowels('Beautiful day', True) -> 7
# count_vowels('rhythm') -> 0
# count_vowels('rhythm', True) -> 1

# c=0
# def count_vowels(text, with_y=False):
#     if with_y == 'True':
#      for char in text:
#          if char in 'aeiouy':
#              global c
#              c+=1
#     else:
#         for char in text:
#             if char in 'aeiou':
#                 c+=1
# count_vowels(input(),input())
# print(c)


#
# Напишите функцию count_signs(nums),
# которая принимает список чисел и
# возвращает кортеж из двух значений: количество положительных чисел и количество отрицательных.
# Нули не учитываются ни в одном из счётчиков,
# поэтому для списка из одних нулей функция возвращает (0, 0).
# Примеры вызова:
# count_signs([1, -2, 3, -4, 5]) -> (3, 2)
# count_signs([0, 0, 0]) -> (0, 0)
# count_signs([-7, -8]) -> (0, 2)

#
# s = [0,0]
# def count_signs(nums):
#     for i in nums:
#         if int(i) > 0:
#             global s
#             s[0]  += 1
#         elif int(i) < 0:
#             s[1] += 1
# count_signs(input().split())
# print(tuple(s))




# def average_of_list(nums,digits =2):
    #   if not nums:
    #    return 0
#     a = sum(nums)/len(nums)
#     round(a,digits)
#     return a
# print(average_of_list([4,5,5,6],1))





# Напишите функцию unique_items(values),
# которая принимает список и возвращает множество его уникальных элементов.
# Если список пуст, функция возвращает строку "Список пуст".
# Примеры вызова:
# unique_items([1, 2, 2, 3, 1]) -> {1, 2, 3}
# unique_items([7, 7, 7]) -> {7}
# unique_items([]) -> 'Список пуст

# def unique_items(values):
#     if values:
#         s = set(values)
#         return s
#     return 'none'
# print(unique_items([]))




# def number_squares(n):
#     if n < 1:
#         return 'none'
#     s = []
#     if n>=1:
#      for i in range(1,n+1):
#         s.append(i**2)
#      return s
#
# print(number_squares(5))






