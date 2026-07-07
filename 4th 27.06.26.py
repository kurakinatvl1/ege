# ph = input()
# # a = float(input())
# # pi = 3.14
# # if ph == 'круг' :
# #     print(a**2*pi)
# # else :
# #     print(a**2)


# n = int(input())
# a = n // 1000
# b =(n // 100) % 10
# c = (n // 10) % 10
# d = n % 10
# print(a, b, c, d)
# if a+b == c+d:
#     print("YES")
# else:
#     print("NO")


# a1, b1 = 1 , 5
# a2 , b2 = 3 , 8
# if a1>a2:
#     left = a1
# else:
#     left = a2
#
# if b1<b2:
#     right = b1
# else:
#     right = b2
#
# if left<right:
#     print('пересекаются в:', left,right)
# elif left == right:
#     print('пересекаются в точке', left)
# else:print('не пересекаются')


# m = str(input())
# n = int(input())
# if (input == 'jan' or 'mar' or 'may' or 'jul' or 'aug' or 'oct'or 'dec') and 1<n<=31:
#     print('correct')
# elif 1<n<=30 and (input == 'apr' or 'jun' or 'sep' or 'nov'):
#      print('correct')
# elif 1<n<=28 and (input == 'feb' ):
#      print('correct')
# else:
#     print('error')

# n1 = 1
# n2 = 2
# match n2:
#     case 4,6,9,11:
#         if 1<=n1<=30:
#           print('correct')
#         else:
#             print('error')
#     case 1, 3 , 5 , 7 , 8 , 10 ,12:
#         if 1 <= n1 <= 30:
#          print('correct')
#         else:
#          print('error')
#     case 2:
#         if 1 <= n1 <= 30:
#          print('correct')
#         else:
#          print('error')
#     case _:
#          print('error')


# x = int(input())
# n = int(input())
# if n == 50 or n == 100 or n == 200:
#  if x>n:
#     print('insufficient funds')
#  else:
#      change = n-x
#      z10 = change//10
#      z5 = (change%10)//5
#      z2 = (change%10)- z5*5 )//2
#      z1 = (change%10)- z5*5 )%2
#
#      print(z10, '- tens,', z5, '- пятерок,', z2, '- двоек,', z1, 'единиц' )
# else :
#      print('error')

#
# r = int(input())
# t = str(input())
# if 1<=r<= 3 :
#     if t == 'day':
#      print('150r')
#     else:
#      print(150*1.3)
# else:
#     if t == 'day':
#      print((r-3)*20)
#     else:
#      print((r-3)*20*1.3)



# a = 1
# # print(f'dssss {a+a}gggg') #f строки
# s = '{1}dddd{2}yy{0}'.format(' its ',' not ',' bad ')
# s = '{city}ddddyy'.format(city=' its ')
# print(s)


# h = int(input())
# m = int(input())
# s = int(input())
# if 0<=h<=23 and 0<=m<=59 and 0<=s<=59:
#  print(f'{h}:{m}:{s} ')
# else:
#  print('error')



# a1 = 162
# a2 = 168
# a3 = 1
# a4 = 10
# cnt = 0
# if 0<= a1 <= 255:
#     if 0<= a2 <= 255:
#         if 0<= a3 <= 255:
#             if 0<= a4 <= 255:
#                 cnt += 1
# if cnt == 0:
#     print('invalid')
# else:
#   if 1<= a1 <= 126:
#     print('class a')
#   elif 128<= a1 <= 191:
#     print('class b')
#   elif 192 <= a1 <= 223:
#     print('class c')
#   elif a1 == 127 or a1 == 0 or a1 >=223:
#     print('sluzebnyi')
# ip = f'{a1}.{a2}.{a3}.{a4}'
# if (a1 ==  10 and 0<= a2 <=255 ...
