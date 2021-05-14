# reverse() 시간 복잡도 O(N) -> R이라는 명령어가 올때마다 reverse() 메소드를 사용하면 시간초과가 발생
# 문제해결:
#   R이라는 명령어가 올때마다 reverse() 메소드를 사용하는 것이 아닌 상태 값을 두어 D 명령어 시 맨 앞을 pop할지 맨뒤를 pop할지 정해준다.

# join메소드를 사용할때 list에 각 원소가 str형이여야 한다. int형일 경우 오류 발생 !! 주의하자

from collections import deque


def AC(deq, p):
    rev = False

    for i in range(len(p)):
        if p[i] == 'R':
            if not rev:
                rev = True
            else:
                rev = False
        elif p[i] == 'D':
            try:
                if not rev:
                    deq.popleft()
                else:
                    deq.pop()
            except:
                print('error')
                return

    li = list(deq)
    if not rev:
        print('['+','.join(li) + ']')

    else:

        print('['+','.join(li[::-1]) + ']')



T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    arr = input()
    arr = arr.replace('[', '')
    arr = arr.replace(']', '')
    if n > 0:
        deq = deque( arr.split(','))
    else:
        deq = deque()

    #deq = input()[1:-1].split(',') => 한줄로도 가능하다

    AC(deq, p)
