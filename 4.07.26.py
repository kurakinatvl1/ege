# a = abs(int(input()))
# k = 0
# # при делении с остатком всегда исп полжит число
# while a :
#         k += a % 10
#         a = a // 10
# print(k)

# a = input()
# counter = 0
# summ = 0
# while counter < len(a):
#     summ += int(a[counter])
#     counter += 1
# print(summ)

#
# n = float(input())
# d = 0
# while d< n:
#     d += 1
#     if n%d == 0:
#         print(d)

# Выведите квадраты чисел от 1 до 10. Если квадрат больше 50, остановите цикл.
# Если цикл завершился полностью, выведите "Все квадраты меньше 50".
# counter = 0
# while counter < 10 and ((counter+1)**2)<=50:
#     counter += 1
#     print( counter**2)
# print


# counter = 0
# flag = False
# while counter < 10:
#     square = counter ** 2
#     if square > 50:
#         flag = True
#         break
#     print(square)
#     counter += 1
#     ###### if not flag:
#     #     print('се квадраты меньше 50')
#  else : #сработает если не сработал брейк
#  print('dсе квадраты меньше 50')


# n = float(input())
# if n >= 1:
#    j == 1
#    flag = False
#    while n - 1 > j:
#      if n%j == 0:
#       flag = True
# print('sostavnoye')
#    break
# else:
#     print('prostoye')
#
# st = str(input())
# if len(st)>= 5 :
#      counter = 0
#      string = ''
#      while counter < 5 :
#         string == (a[counter])
#         counter += 1
#       print(string)
# else:
#      print('строка слишкм короткая')



# a = abs(int(input()))
# k = 0
# y = 0
# n = 0
# while a:
#     k += a % 10
#     a = a // 10
#
#     if k%2 == 0:
#         y += 1
#     else:
#          n += 1
# print(y, n)


n = int(input())
ev,od = 0,0
while n:
    if n%2 == 0:
        evens += 1
    else:
        odds += 1
    n = n // 10
print(ev, od)


