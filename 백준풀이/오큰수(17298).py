'''
O(N^2)이 걸릴수도 있는 문제를 스택을 사용해 O(N)에 가깝게 만드는 문제.

왼쪽에서부터 값을 스택에 넣으면서 알고리즘을 진행해나가는데 스택에 값을 넣기 전에 스택에 가장 위에 있는 값이 현재의 값보다 작거나 스택이 빌때까지 pop 연산을 해서 빼주고 나서
현재의 값을 스택에 push해 나간다. => 스택의 가장 위의 값이 pop이 되는 순간 바로 해당 인덱스의 오큰수가 현재의 값이 된다는 의미.
(스택에 원소를 넣을때 해당 값의 인덱스를 함께 넣어주어야 스택에서 pop을 하면서 오큰수를 업데이트하는데에서 시간을 줄일 수 있음)

'''


N = int(input())
numbers = list(map(int, input().split()))

answer = [-1] * N
stack = []

for i in range(N):
    while stack and (stack[-1][0] < numbers[i]):
        tmp, idx = stack.pop()
        answer[idx] = numbers[i]
    stack.append((numbers[i], i))

print(*answer)