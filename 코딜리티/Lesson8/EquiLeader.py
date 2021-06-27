# 제일 처음 전체 값을 오른쪽 딕셔너리에 넣어 빈도수를 만든 후,
# for 문을 하나씩 돌면서 오른쪽 딕셔너리는 빼서 왼쪽 딕셔너리에 추가한다.
# 추가하면서, 좌측에서 제일 큰 값이 우측에서도 도출해 내고, 둘다 전체 중에 반을 넘는 지 확인하면서, count를 1씩 증가

def solution(A):
    count = 0

    right_dict = {}
    right_len = len(A)
    for a in A:
        if a in right_dict:
            right_dict[a] += 1
        else:
            right_dict[a] = 1

    left_leader = 0
    left_leader_count = 0
    left_dict = {}
    left_len = 0

    for a in A:

        right_dict[a] -= 1
        right_len -= 1

        if a in left_dict:
            left_dict[a] += 1
        else:
            left_dict[a] = 1
        left_len += 1

        if left_dict[a] > left_leader_count:
            left_leader = a
            left_leader_count = left_dict[a]

        if left_leader_count > left_len / 2 and right_dict[left_leader] > right_len / 2:
            count += 1

    return count