import sys; sys.stdin = open('1759_input.txt', 'r')


def solve(k, s):
    global ja, mo
    if k == L:
        if mo >= 1 and ja >= 2:
            print(''.join(arr))
        return
    for i in range(s, len(alphabet)):
        alp = alphabet[i]
        if not visited[i]:
            visited[i] = 1
            arr.append(alp)
            if alp in 'aeiou':
                mo += 1
            else:
                ja += 1
            solve(k + 1, i)
            if alp in 'aeiou':
                mo -= 1
            else:
                ja -= 1
            arr.pop()
            visited[i] = 0


L, C = map(int, input().split())
alphabet = sorted(list(input().split()))
visited = [0] * len(alphabet)
arr = []
ja = 0
mo = 0
solve(0, 0)
