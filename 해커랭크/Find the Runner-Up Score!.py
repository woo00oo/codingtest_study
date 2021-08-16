if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    top1 = arr.pop()
    while True:
        if top1 != arr[-1]:
            print(arr[-1])
            break
        else:
            arr.pop()
# 키 체인 테스트