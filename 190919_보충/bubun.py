path = [0] * 3 # 원소의 수만큼 선택을 하므로, 원소의 수만큼 경로가 필요
def subset(k, n):
    if k == n:
        print(path)
        return
    # 함수 호출이 선택이다.
    path[k]=-1; subset(k+1, n)
    path[k]=1; subset(k+1, n)

subset(0, 3)