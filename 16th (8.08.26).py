# Датчики ТЦ отдают ряд парковочных мест:
#  spots = [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1]
#  (1 — занято, 0 — свободно). Табло должно показать самый длинный отрезок свободных мест подряд и номер места, с которого он начинается.

# spots = [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1]
# amount_places = 0
# starts = 0
# cur_len = 0
# cur_start= 0
# for i in range(len(spots)):
#     if spots[i]==0:
#         if cur_len ==0:
#             cur_start = i
#         cur_len += 1
#     else:
#         cur_len = 0
#     if cur_len > amount_places:
#         amount_places = cur_len
#         starts = cur_start
# print(amount_places,'- свободных с места',starts+1)
# answ- 4,9






#
#
# Рейтинг автомата хранится по убыванию:
# rating = [9800, 9500, 8700, 8100, 7600].
# Игрок набрал 8900. Вставьте результат на
# правильную позицию (без сортировки — она
# пересортирует всё, а нужно лишь найти место)
# и объявите игроку его место.

# rating = [9800, 9500, 8700, 8100, 7600]
# score = 8900
# place = 0

# rating.reverse()
# for i in range(len(rating)):
#     if score < rating[i]:
#         rating.reverse()
#         place = i
#         rating.insert(i-1, score)
#         break
# print(rating,place)






# !!!!! кортежи,tuple()

# a = (1,'i',3,[],{})
# b,c=10,20
#
# # r = (20,10,20)
# c = (1,2,3,4)
# # d = r+c
# # d = (*c,*r)
# # print(d)
# s1,*s2,s3 = c
# print(s1,s2,s3)

# b = (1,[2,3,4],5)
# s,(s1,*s2),s3 = b
# print(s,s1,s2,s3)

# !!  * - оператор распаковки/упаковки,т словарика только ключи

# b = [(1,2),(3,4)]
#1/ for i in b:
#     print(sum(i)) or (i[0]+i[1])
#
# 2/for i,j in b:
#     print(i+j)


# n = [([1,2],3),['xy',6]]
# for (i,i1),j in n:
#     print(i,i1,j)

#
# t = (10,20,30,40)
# t1,*t2 = t
# print(t1,t2)

# s = ()
# n = tuple(input().split())
# d = s+n
# *rest,last = d
# rest.reverse()
# rest = tuple(map(int,rest))
# print(last,rest)


# a = tuple(map(int, input().split()))
# a = a[::-1]
# last,*rest = a
# print(last,rest)
#
# a = (10,20,30,40)
# b = (1,2,3,4)
# c = []
# for i in range(len(a)):
#     c1= a[i]+b[i]
#     c.append(c1)
#
# print(tuple(c))