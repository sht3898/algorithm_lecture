n = int(input())
two = 0
five = 0
for i in range(2, n+1):
    temp = i
    while not (temp % 5):
        five += 1
        temp /= 5
    while not (temp % 2):
        two += 1
        temp /= 2
        
print('0의 개수')
if two < five:
    print(two)
else:
    print(five)