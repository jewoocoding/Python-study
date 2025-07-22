# 집합

s1 = set([1,2,3])
print(s1)
print(type(s1))
s1 =  {1, 2, 3}
print(s1)
print(type(s1))
s2 = set("Hello")
print(s2)
print(s1 & s2) # 교집합
print(s1.intersection(s2))

# 합집합
print(s1 | s2)
print(s1.union(s2))

#차집합
print(s1 - s2)
print(s1.difference(s2))

#값 추가
s1.add(123)
print(s1)
# 여러개 추가
s1.update([4, 3, 1])
print(s1)
#제거
s1.remove(123)
print(s1)