# 1.
# В чате курса работает бот: сообщение удаляется, если содержит слово из чёрного списка.
# Постройте очищенный чат и посчитайте удалённые сообщения.


#//if 1 word in black list:
# chat = ["Привет мир", "спам ...", "Hello World", "СПАМ",'Привет Спам']
# black_list = 'спам'
# c = 0
# clean_chat = []
# for i in chat:
#     i2=i.lower()
#     if black_list in i2:
#             c+=1
#     else:
#            clean_chat.append(i)
# print(c,clean_chat)


#// if >1 word in black list:
# chat = ["Привет мир", "спам ...", "Hello World ", "СПАМ",'Привет Спам','a б в ']
# black_list = ['спам','a']
# c = 0
# clean_chat = []
#
# for i in chat:
#     flag = True
#     i2=i.lower()
#     for j in black_list:
#         j2=j.lower()
#         if j2 in i2:
#            flag = False
#     if flag:
#            clean_chat.append(i)
#     else:
#         c+=1
# print(c,clean_chat)



# 2.
# Цены акции за 8 дней:
#  prices = [270, 265, 280, 242, 268, 275, 290, 285]
# . Если бы можно было один раз купить и один раз продать (продажа строго после покупки)
# — в какие дни это стоило сделать и какова максимальная прибыль? Переберите все пары «день покупки — день продажи».
#
# prices = [270, 265, 280, 242, 268, 275, 290, 285]
# res = 0
# buy = 0
# sell = 0
# for i in range (len(prices)):
#     for j in range (i+1,len(prices)):
#         if prices[j] > prices[i]:
#             a = prices[j]-prices[i]
#             if a > res:
#                 res = a
#                 buy = i+1
#                 sell = j+1
# print(res,buy,sell)
#answer - 48,4,7


#
# 3.
# Баллы участников:
#  scores = [85, 92, 85, 100, 78]
# . Присвойте каждому место по правилу спортивного рейтинга:
# место = 1 + количество участников со строго бо‌льшим баллом. Тогда набравшие поровну автоматически делят одно место.
# scores = [85, 92, 85, 100, 78]
# for i in scores:
#     a = 1
#     for j in scores:
#         if j>i:
#             a += 1
#     print(i,'place',a)





#
# 4.
# Датчики ТЦ отдают ряд парковочных мест:
#  spots = [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1]
#  (1 — занято, 0 — свободно). Табло должно показать самый длинный отрезок свободных мест подряд и номер места, с которого он начинается.

# spots = [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1]
# c = 0
# n = 0
# for i in range(len(spots)):
#     if spots[i]==0:
#         c2 = 1
#         for j in range(i+1,len(spots)):
#             if spots[j]!=0:
#                 break
#             c2 +=1
#             if c2>c:
#                  c = c2
#                  n = i+1
# print(c,'- свободных с места',n)
# answ- 4,9