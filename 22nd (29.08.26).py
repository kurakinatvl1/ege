



# def max_streak(data,value):
#     counter = 0
#     max_i = 0
#     max_streak = 0
#     for i in range(len(data)-1):
#         if data[i] == value:
#             counter += 1
#             if counter > max_streak:
#                 max_streak = counter
#                 max_i = i
#         else:
#             counter = 0
#     return max_streak,max_i- max_streak+1
# print(max_streak(['+', '-', '-', '+', '-', '-', '-', '+'], '-'))
from gettext import find

# def  to_binary(n, width=8):
#     if n < 0:
#         return 'Только неотрицательные числа'
#     res = bin(n)[2:]
#     b = 0
#     if len(res) < width:
#         b = (width - len(res))
#     d = '0'*b + res
#     return d
# print(to_binary(5))




# Напишите функцию is_prime(n),
# которая принимает целое число и возвращает True для простых чисел или False для чисел,
# не являющихся простыми.
# n = int(input())
# def is_prime(n):
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#         else:
#             return True
# print(is_prime(n))

#
# n = int(input())
# def is_prime(n):
#   if n <= 2:
#     return False
#   for i in range(2, int(n**0.5) + 1):
#     if n % i == 0:
#       return False
#   return True
# print(is_prime(n))








# 24. Напишите функцию `binary_search(lst, target)`,
# которая принимает отсортированный список и искомый элемент и возвращает индекс найденного элемента.
# Если элемент не найден, возвращает -1
# lst = sorted(list(map(int, input().split())))
# target = int(input())
# def binary_search(lst, target):
#     for i in range(len(lst)):
#         if lst[i] == target:
#             return i
#     return -1
# print(binary_search(lst, target))


# lst =[1,3,4,60,55,2]
# lst = sorted(lst)
# def binary_search(lst, target):
#     right = len(lst) - 1
#     left = 0
#     while left <= right:
#         mid =(right+left)//2
#         if lst[mid] == target:
#             return mid
#         elif target > lst[mid]:
#             left = mid + 1
#         elif target < lst[mid]:
#             right = mid - 1
#     return -1
# print(binary_search(lst, 60))





# Напишите функцию camel_to_snake(s),
# которая принимает строку в «верблюжьем регистре» (ThisIsCamelCased) и
# преобразует ее в «змеиный регистр» (this_is_camel_cased).
# Добавьте аргумент separator с значением по умолчанию _,
# чтобы функция также могла преобразовывать в «кебаб-регистр» (this-is-camel-case).
# s = 'ThisIsCamelCased'
#
# def camel_to_snake(s,separator='_'):
#     # i = 0
#     # while i< len(s):
#     #     if s[i].isupper():
#     #         s = s.replace(s[i], (s[i]+separator))
#     #     i +=1
#
#     result = ''
#     for char in s:
#         if char.isupper():
#             result += separator + char.lower()
#         else:
#             result += char
#     if result[0]== separator:
#         result = result[1:]
#     return result
# print(camel_to_snake(s))










