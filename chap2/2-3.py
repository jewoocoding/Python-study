#리스트
odd = [1,3,5,7,9]
print(type(odd))
# 자료형 상관없이 담을 수 있음
print(odd[0])

#이중 리스트
a = [1, 2, 3, ['a', 'b' , 'c']]
print(a[3][1])

# 슬라이싱
print(a[0:2])

#리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

#리스트 길이 
print(len(a))


a[2] = 4
print(a)
del a[1]
print(a)

a.append(23)
print(a) 

a.sort() #정렬
print(a)
a.reverse()
print(a)

#리스트에 요소 삽입
a.insert(0,11111) # 0번째 인덱스에 11111 삽입
print(a)

#리스트 요소 제거
a.remove(1)
print(a)

print(a.pop())
print(a)

a.append([4, 5])
print(a)
a.extend([4, 5])
print(a)