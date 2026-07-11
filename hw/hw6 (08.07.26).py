
# 1.
# *
# **
# ***
# ****
# ***
# **
# *

# z = '*'
# n = 8
# for x in range(n):
#         if x<=4:
#             print(z*x)
#         else:
#             print(z*(n-x))



# 2.
# @@@@@
# @@@@@
# @@@@@
# @@@@@
# @@@@@

# z = '@@@@@'
# for i in range(5):
#     print(z)


# 3.
# ***
# * * *
# ** **
# * * *
#  ***
#//////если есть пробел в конце
# n = 3
# z = '***'
# a = '* * *'
# b = '** **'
# for i in range(n):
#     if i==1:
#         print(b)
#     elif i<1:
#         print(z)
#         print(a)
#     else:
#         print(a)
#         print('',z)


#/////если нет пробела
n = 5
z = '***'
a = '* * *'
b = '** **'
for i in range(n):
    if i==2:
        print(b)
    elif i==0 or i==4:
        print(z)
    else:
        print(a)


# 4.

#   +
#   +
# +++++
#   +
#   +

# z = '+'
# for i in range(5):
#     if i == 2:
#         print(z*5)
#     else:
#         print(' ',z)
