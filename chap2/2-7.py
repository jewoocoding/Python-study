#boolean
a = 1 < 2
print(a)

#자료형의 참과 거짓
# 있으면 참, 없으면 거짓
# 1: true, 0: false
# none : false

a = [1,2,3,4]
while a:
    print(a)
    a.pop()
print("finish")

if [1,2,3] : 
    print("참")
else:
    print("거짓")

a = bool([1,2,3])
print(a)

a, b = ('python', 'life')
print(a)
print(b)

a = b = 'python'
print(b)