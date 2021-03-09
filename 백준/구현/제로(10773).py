K = int(input())
Stack = list()
for _ in range(K):
    number = int(input())
    if number != 0:
        Stack.append(number)
    else:
        Stack.pop()
print(sum(Stack))
