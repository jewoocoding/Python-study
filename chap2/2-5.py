# 딕셔너리(map : key - value)

dic = {'name' : 'jewoo', 'birth' : "981222", 'a' : [1, 2,3]}
print(dic)

# 요소 삭제
del dic['name']
print(dic)

print(dic['a'])

print(dic.keys()) # key들의 리스트 생성
print(dic.items())
# dic.clear()
# print(dic)
print(dic.get("a"))
print('name' in dic)