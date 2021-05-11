# 리스트 슬라이싱을 사용

while True:
    N = input()
    if N == '0':
        break
    N_rev = N[::-1]
    if N == N_rev:
        print("yes")
    else:
        print("no")