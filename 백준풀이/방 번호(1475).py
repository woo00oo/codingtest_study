# 1set에서 가장 많이 나온 수가 정답
# 하지만 6 <-> 9 로 변환이 가능하기 때문에
# 6이 나온 수 와 9가 나온 수를 더해서 2로 나눈다 나머지가 0이라면 몫이 필요한 세트 수고, 아니면 몫에다가 1을 더해준다.
# 6, 9 를 만들기 위해 필요한 개수와 일반적인 거를 만들기 위한 필요한 개수중 큰 것이 정답

room_number = input()

number_count = [0] * 10

sixnine = 0

for i in range(10):
    if i == 6 or i == 9:
        number_count[i] = 0
        sixnine += room_number.count(str(i))
    else:
        number_count[i] = room_number.count(str(i))

max_number = max(number_count)

if sixnine % 2 == 0:
    sixnine //= 2
else:
    sixnine = sixnine // 2 + 1

answer = max(sixnine, max_number)
print(answer)