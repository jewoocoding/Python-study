#range
add = 0
for i in range(1, 11):
    add = add + i
print(add)

for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')

a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)