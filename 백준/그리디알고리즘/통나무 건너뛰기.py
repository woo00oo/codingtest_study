#문제 해결:
# 입력받은 리스트를 오름 차순으로 정렬
# 정렬 된 리스트의 맨 앞 원소부터 리스트의 맨앞, 맨뒤 를 반복하여 배치 시킨다.
# 이렇게 배치된 리스트가 최소 난이도를 구할수 있는 리스트가 됨
# ex) 1,2,3,4,5,6,7
# ex) 1 0 0 0 0 0 2
# ex) 1 3 0 0 0 4 2
# ex) 1 3 5 0 6 4 2
# ex) 1 3 5 7 6 4 2

test_case_num = int(input())

for _ in range(test_case_num):
    N = int(input())
    height_list = sorted(list(map(int,input().split())))
    min_height_list = [0] * N
    front, rear = 0, 1
    answer = 0

    for index in range(N):
        if index % 2 ==0:
            min_height_list[front] = height_list[index]
            front += 1
        else:
            min_height_list[-rear] = height_list[index]
            rear += 1
    for i in range(N):
       answer = max(answer,abs(min_height_list[i]-min_height_list[i-1]))
    print(answer)
