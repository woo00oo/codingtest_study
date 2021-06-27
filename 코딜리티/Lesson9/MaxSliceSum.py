def solution(A):
    # 슬라이스 한 합을 위함
    slice_sum = [0]
    # 슬라이스 최대 합을 위함
    m = float('-inf')
    # a의 변수의 최대를 위함
    n = float('-inf')

    for a in A:
        c = slice_sum[-1] + a

        # 모든 값이 음수일 경우, 음수중에 가장 큰 값을 가져오기 위함
        if n < a:
            n = a

        # 슬라이스 합이 -로 갈경우는 0으로 초기화
        if c < 0:
            slice_sum.append(0)
        else:
            slice_sum.append(c)
            # 중간 중간 초기화가 되기때문에, 최댓값을 저장해놓기 위함
            if m < c:
                m = c

    # 모두 음수일 경우 0이 return되기 때문에 배열 A중에 가장 큰 요소 하나를 return
    return m if 0 < m else n