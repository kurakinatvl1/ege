


# Напишите функцию check_login(name, min_len=5) для проверки логина.
# Функция возвращает True, если логин корректен, и строку с причиной отказа, если нет.
# Правила: длина не меньше min_len символов (иначе "Слишком короткое имя"),
# первый символ — буква (иначе "Имя должно начинаться с буквы"),
# остальные символы — только латинские буквы, цифры и подчёркивание (иначе "Недопустимый символ").
# Примеры вызова:
# check_login('user_2024') -> True
# check_login('abc') -> 'Слишком короткое имя'
# check_login('1user') -> 'Имя должно начинаться с буквы'
# check_login('user name') -> 'Недопустимый символ'
# def check_login(name, min_len=5):

#     if len(name) < min_len:
#         return "Слишком короткое имя"
#     elif not (name[0].isalpha()):
#         return "Имя должно начинаться с буквы"
#     else:
#         for i in name:
#             if not (i.isalpha() or i.isdigit() or i=='_'):
#                  return "Недопустимый символ"
#     return True
# print(check_login('user_2024'))
# print(check_login('abc'))
# print(check_login('1user'))
# print(check_login('user name'))




#
#
# # Напишите функцию shift_list(items, k, direction="right"),
# # которая принимает список, число k и направление сдвига и возвращает новый список
# # — результат циклического сдвига на k позиций (по умолчанию вправо).
# # Используйте только срезы.
# # Если k больше длины списка, сдвиг выполняется по остатку от деления, а для пустого списка функция возвращает пустой список.
# # Примеры вызова:
# # shift_list([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
# # shift_list([1, 2, 3, 4, 5], 2, 'left') -> [3, 4, 5, 1, 2]
# # shift_list([], 3) -> []
# def shift_list(items, k, direction="right"):
#     if not items:
#         return []
#     if direction == "right":
#             shifted_items = items[k:]+items[:k]
#             return shifted_items
#     else:
#             k = k % len(items)
#             shifted_items = items[-k:]+items[:-k]
#             return shifted_items
#
# print(shift_list([1, 2, 3, 4, 5], 2))
# print(shift_list([], 3))
# print(shift_list([1, 2, 3, 4, 5], 2, 'left'))






# На складе два словаря вида "товар — количество".
# Напишите функцию merge_stocks(stock1, stock2, min_amount=0),
# которая принимает два словаря и возвращает новый словарь с суммарным количеством каждого товара.
# В итоговый словарь попадают только товары, которых не меньше min_amount штук (по умолчанию 0, то есть попадают все).
# Примеры вызова:
# merge_stocks({'яблоки': 10, 'груши': 5}, {'бананы': 8, 'яблоки': 3}) -> {'яблоки': 13, 'груши': 5, 'бананы': 8}
# merge_stocks({'яблоки': 10, 'груши': 5}, {'бананы': 8, 'яблоки': 3}, 9) -> {'яблоки': 13}
# merge_stocks({}, {'сливы': 4}) -> {'сливы': 4}

def merge_stocks(stock1, stock2, min_amount=0):
    res  = stock1.copy()
    for x,y in stock2.items():
        if x not in res.keys():
            res.update({x:y})
        else:
            res[x]+= y
    res1 = res.copy()
    for (x,y) in res1.items():
        if res1[x] < min_amount:
            res.pop(x)
    return res

print(merge_stocks({'яблоки': 10, 'груши': 5}, {'бананы': 8, 'яблоки': 3},9))
print(merge_stocks({}, {'сливы': 4}))







