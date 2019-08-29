arr = '123456'

val = 0
for c in arr:
    val = val * 10 + (ord(c) - ord('0'))

print(val)
print(type(val))

val_str = ''
while val:
    print(val % 10)
    val = (val//10)