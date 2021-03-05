#문제풀이:
#   주사위의 면이 1면만 보이는 경우, 2면이 보이는 경우, 3면이 보이는 경우로 나눠서 생각한다.
#   1면이 보이는 주사위의 개수는 = (n-2)*(n-2) + 4*(n-1)*(n-2)개
#   2면이 보이는 주사위의 개수는 = (n-2)*(n-2) + 4*(n-1)*(n-2) 개
#   3면이 보이는 주사위의 개수는 = 정육면체 최상단의 각 꼭짓점으로 4개이다.

#   주사위의 특성상 마주보는 면을 제외하고 모든 면이 인접해있음
#   A와 F(0과 5) B와 E(1과 4) C와 D(2와 3)중 최소 값을 리스트에 저장하고
#   1면, 2면, 3면의 경우에 따라 더 작은 것부터 더해서 사용하면 된다.

n = int(input())
numbers = list(map(int,input().split()))
Sum = 0
SumLists = list()
if n==1:
    numbers.sort()
    for i in range(5):
        Sum += numbers[i]
else:
    SumLists.append(min(numbers[0],numbers[5]))
    SumLists.append(min(numbers[1],numbers[4]))
    SumLists.append(min(numbers[2],numbers[3]))
    SumLists.sort()

    # 1,2,3면이 보여질때 주사위 최소값
    min1 = SumLists[0]
    min2 = SumLists[0] + SumLists[1]
    min3 = SumLists[0] + SumLists[1] + SumLists[2]

    # 1,2,3면이 보여지는 주사위 개수
    n1 = (n-2)*(n-2) + 4*(n-1)*(n-2)
    n2 = 4*(n-2) + 4*(n-1)
    n3 = 4

    Sum += n1 * min1
    Sum += n2 * min2
    Sum += n3 * min3

print(Sum)