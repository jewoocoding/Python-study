# 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)
arr = [a, b, c]

for i in arr :
    if i % 2 == 0 :
        print("even")
    else :
        print("odd")