# fantasy_readers = {"Игорь", "Катя", "Лев", "Марина"}
# detective_readers = {"Катя", "Лев", "Никита", "Ольга"}
# sci_fi_readers = {"Лев", "Марина", "Никита", "Павел"}
#
# a = fantasy_readers & detective_readers & sci_fi_readers
# s1 = fantasy_readers & detective_readers
# s2 = fantasy_readers & sci_fi_readers
# s3 = sci_fi_readers & detective_readers
# s4 = (s1 | s2|s3) - a
# print(s4)
# s1.



# intersection &
# difference -
# update union |



# football_players = {"Алексей", "Богдан", "Вика", "Дарья"}
# basketball_players = {"Богдан", "Вика", "Егор", "Зоя"}
# volleyball_players = {"Вика", "Дарья", "Егор", "Ирина"}

# s1 = football_players - basketball_players - volleyball_players
# s2 = basketball_players - volleyball_players - football_players
# s3 = volleyball_players - football_players - basketball_players
# s4 = s1|s2|s3
# print(s4)


#
# s = 'hello world hi spam SPA peace'
# black_l = {'spam','spa'}
# blocked = []
# s = set(s.lower().split())
# //1
# for i in s.copy():
#     if i in black_l:
#         s.remove(i)
#         blocked.append(i)
# print(s,'blocked:',blocked)

# # //
# s = set(s.lower().split()) & black_l
# print(s)



# busy = {("pn", 10), ("pn", 12), ("vt", 10), ("sr", 16)}
# want = [("pn", 10), ("sr", 14), ("vt", 10), ("pt", 12)]
# //1
# sv = set(want) - busy
# print(sv)
# //2
# for i in want:
#     if i not in busy:
#         print(i)





# !!!!! dict  - итерирукмьй , индесируемый по keys
# d = {key:value}
# d['key'] = 10 # mapping
# #
# d = {
#     'key1':'value1',
#     'key2':'value2',
#     'key3':'value3'
# }
#

# s1 = s.copy()
# d.update({
#     'key1':'1',
#     'key5':'5'
# })
# print(d)


# print(d.popitem()) # deletes and returns last element(items)
# print('key1' in d)

# d['key4'] = 10  #add key and value
# d['key3'] = 20 # changes value of the key, that had already existed
# del d['key2'] # delete element
# print(d)

# print(d.get('key1',100)) #always use get,so there will be no error.
# if there is a key then returns value,if not then default
# d.pop('key3')  # delete an element by its key
# print(list(d.items()))
# print(list(d.keys())) # list of keys



#
# d = []
# s = input().split()
# for  i in s:
#     key,value = i.split(':')
#     # d[key] = value
#     d.append((key,value))
#     dict(d)
# print(d)

#



# st = ['anna',5,'boris',4,'vera',5]
# d = {}
# for i in range (0,len(st),2):
#   d[st[i]] = st[i+1]
# print(d)





