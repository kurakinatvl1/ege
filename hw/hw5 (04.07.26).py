# # Пользователь вводит строку. На экран выводится эта строка без гласных букв латинского алфавита.
# # (AEIOUaeiou)
# st = input()
# b = 'AEIOUaeiou'
# c = 0
# rez = ''
# while c < len(st):
#     i = st[c]
#     if i not in b:
#        rez += i
#     c+= 1
# print(rez)


# # Пользователь вводит число. Найдите его первый делитель, отличный от 1. Если делителей нет, выведите "Число простое".
# n = int(input())
# counter = 0
# d = 1
# while counter < n and n>1:
#     d+=1
#     if n%d == 0:
#         if d == n:
#             print('prostoye')
#         else:
#             print(d)
#         break
# else:
#     print('prostoye')

#
# # Выведите на экран представленные символы с помощью циклов.
# # *
# # **
# # ***
# # ****
# # *****
# # ******

# z = '*'
# st = ''
# while len(st) < 6:
#     st += z
#     print(st)
