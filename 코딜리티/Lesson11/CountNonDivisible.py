def solution(A):
    N = len(A)
    # 배열 A의 원소갯수를 담을 list, index가 원소가 됨
    element = [0] * (2 * N + 1)

    # 배열 A에서 각 원소갯수를 카운트
    for a in A:
        element[a] += 1

    answer = [0] * N

    # A를 for문돌다가 똑같은 요소인 경우 저장해서 바로 사용하기 위함
    saved = [-1] * (2 * N + 1)
    for i in range(N):
        current = A[i]

        # 이전에 똑같은 원소가 나온 경우
        if saved[current] != -1:
            answer[i] = saved[current]
        else:
            count = 0

            # 현재 원소의 약수를 구하기 위하여, 만약 6인 경우 1,2,3,6이니 2까지만 for문을 돌고 3은 동시에 카운트
            for j in range(1, int(current ** 0.5) + 1):
                if current % j == 0:
                    count += element[j]

                    # current가 4인경우 j가 2인 상황을 위함. 1,2,3,6일 때 2와 3처럼 대칭인 부분이 없기때문
                    if j != current // j:
                        count += element[current // j] # 대칭인 부분까지 count 증가

            # 양수를 구한 후 전체 값을 빼면, 원하는 답이 나옴
            answer[i] = N - count
            # 원소를 저장했다가 중복되는 경우 똑같은 값으로 사용하기 위함
            saved[current] = answer[i]

    return answer