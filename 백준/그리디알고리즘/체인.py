n = int(input())
nList = list(map(int, input().split()))
nList.sort()

ans = 0
while True:
    if len(nList) == 1:  # 하나로 연결되었다면
        print(ans)
        break
    nList[0] -= 1  # 고리 하나 제거
    ans += 1

    if not nList[0]:  # 다 제거했으면
        nList.pop(0)  # 이제 고려하지 않음
    if len(nList) >= 2:
        a = nList.pop()  # 맨 뒤의
        b = nList.pop()  # 두개 제거해서
        nList.append(a + b)  # 하나로 만들어줌