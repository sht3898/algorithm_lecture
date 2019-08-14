import sys
sys.stdin = open('GNS.txt', 'r')

tc = int(input())

for t in range(tc):
    test, n = input().split()
    n = int(n)
    arr = list(input().split())
    result = []
    answer = []
    gns = ''
    num_dict = {
        "ZRO": 0,
        "ONE": 1,
        "TWO": 2,
        "THR": 3,
        "FOR": 4,
        "FIV": 5,
        "SIX": 6,
        "SVN": 7,
        "EGT": 8,
        "NIN": 9
    }
    new_num = {
        0: "ZRO",
        1: "ONE",
        2: "TWO",
        3: "THR",
        4: "FOR",
        5: "FIV",
        6: "SIX",
        7: "SVN",
        8: "EGT",
        9: "NIN"
    }
    for num in arr:
        result.append(num_dict[num])
    result = sorted(result)
    for idx in result:
        answer.append(new_num[idx])
    for num1 in answer:
        gns += num1 + ' '
    gns = gns[:-1]
    print(test)
    print(gns)