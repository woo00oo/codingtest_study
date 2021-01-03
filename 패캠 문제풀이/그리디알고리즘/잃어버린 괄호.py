# 접근 방법이 잘못 되었다. 괄호를 굳이 쳐주면서 식을 만들어줄 필요가없다.
#
# operation = list(input())
#
# bracket = False
# index = 0
# while True:
#     if index == len(operation):
#         break
#     if operation[index] == '-':
#         if not bracket:
#             operation.insert(index+1,'(')
#             bracket = True
#
#         else:
#             operation.insert(index,')')
#             bracket = False
#
#     index+=1
#
# if bracket:
#     operation.append(')')
# operation = ''.join(operation)
# new = operation.strip('0')
# min_sum = eval(operation)
# print(min_sum)

#문제 해결 능력:
#   마이너스를 만날때 가장 큰수를 빼면된다.
#   마이너스 기호를 만날때 다음 마이너스까지 , 다음 마이너스가 없다면 끝까지 모든 수를 더해서 한번에 빼주면 정답.

operation = input().split('-')
min_sum = 0
for i in operation[0].split('+'):
    min_sum += int(i)
for i in operation[1:]:
    for j in i.split('+'):
        min_sum -= int(j)
print(min_sum)
