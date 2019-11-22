a = list(input())
b = list(input())
c = input()
temp1 = temp2 = temp3 = []
vow = ['a','e','i','o','u']
for i in range(len(a)):
    if a[i] in vow:
        a[i] = '#'
for i in range(len(b)):
    if b[i] not in vow:
        b[i] = '%'
print(''.join(a),end='')
print(''.join(b),end='')
print(c.upper())
        
