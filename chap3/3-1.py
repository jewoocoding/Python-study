# 조건문
money = True
if money :
    print("택시")
else:
    print("뚜벅")


x = 3
y = 2
print(x > y)


money = 2000
card = True
if money > 3000 or card: 
    print("택시")
else:
    print("걸어가라")

# in, not in
print(1 in [1, 2, 3])

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("taxi")
else:
    print("walk")

# pass : 아무것도 안 함
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print("walk")

# elif
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("taxi")
elif card:
    print("taxi")
else: 
    print("walk")

# 참 if 조건문 else 거짓
score = 100
message = "success" if score >= 60 else "failure"
print(message)