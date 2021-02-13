# 쉬운 문제인데 문제를 끝까지 제대로 파악하지 않아서 삽질... 문제 정확하게 읽고 풀기!

char = input()
N = int(input())
rings = [input() for _ in range(N)]
cnt = 0
for ring in rings:
    ring += ring[:len(char)-1]
    for i in range(len(ring)+1-len(char)):
        search = ring[i:i+len(char)]
        if search == char:
            cnt += 1
            break

print(cnt)