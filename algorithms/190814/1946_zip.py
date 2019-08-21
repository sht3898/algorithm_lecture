import sys
sys.stdin = open('zip.txt', 'r')

tc = int(input())

for t in range(tc):
    testcase = int(input())
    print('#{}'.format(t+1))
    result = []
    for test in range(testcase):
        alpha, num = input().split()
        num = int(num)
        for idx in range(num):
            result.append(alpha)
    while len(result) > 0:
        answer = ''
        if len(result) >= 10:
            for idx2 in range(10):
                answer += result[idx2]
        else:
            for idx3 in result:
                answer += idx3
        print(answer)
        result = result[10:]