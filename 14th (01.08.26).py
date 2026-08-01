# text = input()
# text_lower = text.lower()
# for symbol in ".,!?;:-()":
#     text_lower = text_lower.replace(symbol, " ")
# st1 = text_lower.split()
# res1=0
# res2 =''
# for i in st1:
#     res = st1.count(i)
#     if res > res1:
#         res1=res
#         res2 = i
# print(res1, res2)


# !!!!!!!!! списки
# num = [1,2,'df']
# num[0]=10 #изменяемо
# print(num[1:])# срезы
# print(num)

# s = [1,2,3,4,5]
# for i in range(len(s)):
#     s[i] +=1
# print(s)

#len() - колво элементов
#in/not in - принадлежность
#+ - конкатенация
# s = ['hello']+[[1,2,3]]
# print(s)

# index(element) = индекс элемента


# list = [1,2,3,4,5,6]

# print(list.index(9))
# list.append('hello') - добавление элемента в конец списка
# list.extend([1,2,3,4]) - конкатанация
# print(list)
#
# s =[]
# s1 = [1,2,3,4,5,6]
# for i in s1:
#     s.append(i)
# print(s)


# list.insert(2,'nhb') #вставляет обьект отодвтгая последующие символы
# print(list)

# !!! remove - даляет элемент по значению
# print(list.remove(1))

# !!! pop - далениее по индексу
# list.pop(2)
# print(list)

# clear - очищает все элементы(память)

# count - считает колво элементов
# print(list.count(1))

# sort - сортирует
# list= list[::-1]

# list = ['alpha','beta','gkmma','gamma']
# list.reverse()
# list.sort(reverse=True) - сортирует либо по алфавиту либо по порядку
# print(list)

# min/max/sum
#
# nums = [1,-2,3,-4,5,-6,7,-8,9]
# a = 0
# b = 0
# for i in nums:
#     if i > 0:
#         a+=1
#     else:
#         b+=1
# print(a,b)


# l = []
# for i in range(5):
#     l.append(input())
# print(l)

# nums = [1,2,3,4,2]
# first = nums.index(2)
# nums = nums[first+1:]
# print(nums.index(2)+first+1)