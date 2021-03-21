N, K = map(int,input().split())
li = [ i for i in range(2,N+1)]
cnt = 0

while li :
    li.sort()
    Min = li[0]
    removed = 0
    for i in range(len(li)):
        i -= removed
        if li[i] % Min == 0:
            cnt += 1
            if cnt == K:
                print(li[i])
                exit(0)
            del li[i]
            removed += 1