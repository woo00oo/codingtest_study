while True:
    try:
        A,B,C = list(map(int,input().split()))

        count = 0
        while C-A != 2:
            if C-B > B-A:
                A = B
                B = C-1

            else:
                C = B
                B = A+1

            count +=1

        print(count)
    except:
        break