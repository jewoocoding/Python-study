a = "I eat %d apples." % 3
print(a)

a = " %s %s " % ("string","str2")
print(a)

b = "i eat {0} apples".format(10)
print(b)

name = "최제우"
age = 26
a = f'this is string formatting {name} {age + 2}'
print(a)

y = 3.432515
b = f'{y:0.4f}'
print(b)

#문자열 개수 세기
print(a.count('i'))

#문자열 위치 알려주기
print(a.find('i'))
print(a.find("i"))

#문자 삽입
print("-".join(a))

print(a.lower())
print(a.upper())

# 공백지우기
print(a.strip())
print(a.lstrip())
print(a.rstrip())

#문자열 바꾸기
print(a.replace("this","wow"))

#문자열 쪼개기
print(a.split(" "))