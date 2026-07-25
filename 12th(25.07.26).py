# upper/lower
# len/min/max/in
# методы поиска
#    find   - (-1)
#     index - error
# rfind- с обратной стороны

# методы проверки символов
# isupper/islower
# isnumeric / isdigit   - из чисел
# isalnum - строка из цифр и букв, false если есть спец символы и пробел


# разделение строки
# split() - делит по пробелам,возвращает список
# spit('//',1)       or split(',',maxsplit = 1)

# соединение строки
# print(':'.join())


# УДАЛЕНИЕ И ЗАМЕНА
# strip - удаление с концов(по одному символу)
# lstrip/rstrip

# replase('что заменяем','на что заменяем','колво раз')
# replace('f','')       - удаление символа


#count
# s = 'heheh999'
# print(s.count('h',2,10))


# translate()
# print(ord('A'),ord('a'))   - 65 , 97
# table = {
#     ord('a'):ord('@')  ,
#      ord('m'):None
# }

# st = 'hello world. my name'
# result = st.translate(str.maketrans('ae','@3','m'))
# print(result)
#                 st.translate(str.maketrans) -

#
# s = '***helloloooo****'
# h = ''
# for i in range(3):
#     h += s[i]
#
# print(h)


# h  = s[start:end:step]  - ткуда,до куда(не включ),с каким шагом
# s = '***helloloooo****'
# print(s[: :-1]) - переворот в обратн сторону  - list,set,tuple,str


# st = input()
# print(st[:3])

# st = input()
# print(st[-4:])

# print(st[1:-1])


# print(st[:5]+st[-5:])

# print(st[-5:][::-1])


# mid = len(st) // 2

# pr=st[-1:(len(st)//2)]+st[0:(len(st)//2)]
# print(st[mid:][:mid])


# for i in range(len(st)-2):
#     a =st[i:i+3]
#     print(a)

# s = ' шалаш, камыш, заказ, возврат, поиск, довод, спектр, комок, альянс'
# /# s1 = s.replace(' ','')
# /# s2 = s1.split(',')
# s2 = s.split(', ')
# for i in s2:
#     if i[::-1]==i:
#         print(i)

# s = input()
# a = ''
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         sub = s[i:j]
#         if sub == sub[::-1] and len(sub) > len(a):
#          a = sub
# print(a)



