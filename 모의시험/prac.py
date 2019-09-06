# 실패 2
import sys; sys.stdin = open('A_2.txt', 'r')
import pprint

# 0: 상, 1: 하, 2: 좌, 3: 우

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    for i in range(n):
        if arr[i][2] == 0:
            arr[i][0] += 1
            for j in range(n):
                if arr[i][0] == arr[j][0] and arr[i][1] == arr[j][1]:
                    count += 1
                    arr.pop(i)
                    break
        elif arr[i][2] == 1:
            arr[i][0] -= 1
            for j in range(n):
                if arr[i][0] == arr[j][0] and arr[i][1] == arr[j][1]:
                    count += 1
                    arr.pop(i)
                    break
        elif arr[i][2] == 2:
            arr[i][1] -= 1
            for j in range(n):
                if arr[i][0] == arr[j][0] and arr[i][1] == arr[j][1]:
                    count += 1
                    arr.pop(i)
                    break
        elif arr[i][2] == 3:
            arr[i][1] += 1
            for j in range(n):
                if arr[i][0] == arr[j][0] and arr[i][1] == arr[j][1]:
                    count += 1
                    arr.pop(i)
                    break
    print(count)


# 실패 1
# import sys; sys.stdin = open('A_2.txt', 'r')
# import pprint
#
# # 0: 상, 1: 하, 2: 좌, 3: 우
#
# t = int(input())
#
# for tc in range(1, t+1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     visit = []
#     count = 0
#     for _ in range(2000):
#         for i in range(n):
#             print(arr[i])
#             if arr[i][2] == 0:
#                 arr[i][0] += 1
#                 if [arr[i][0], arr[i][1]] in visit:
#                     count += 1
#                     arr.pop(i)
#                 else:
#                     visit.append([arr[i][0], arr[i][1]])
#             elif arr[i][2] == 1:
#                 arr[i][0] -= 1
#                 if [arr[i][0], arr[i][1]] in visit:
#                     count += 1
#                     arr.pop(i)
#                 else:
#                     visit.append([arr[i][0], arr[i][1]])
#             elif arr[i][2] == 2:
#                 arr[i][1] -= 1
#                 if [arr[i][0], arr[i][1]] in visit:
#                     count += 1
#                     arr.pop(i)
#                 else:
#                     visit.append([arr[i][0], arr[i][1]])
#             else:
#                 arr[i][1] += 1
#                 if [arr[i][0], arr[i][1]] in visit:
#                     count += 1
#                     arr.pop(i)
#                 else:
#                     visit.append([arr[i][0], arr[i][1]])
#     print(count)