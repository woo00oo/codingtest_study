# 효율성 검사 실패 : O(N * M)

def solution(S, P, Q):
    answer = []
    M = len(P)

    for i in range(M):
        nucleotides = set(S[P[i]:Q[i]+1])
        if 'A' in nucleotides:
            answer.append(1)
        elif 'C' in nucleotides:
            answer.append(2)
        elif 'G' in nucleotides:
            answer.append(3)
        else:
            answer.append(4)

    return answer

# Prefix sum 알고리즘 문제
# O(N + M)으로 활용 가능
# Prefix sum 이란 데이터베이스를 전처리하여 쿼리의 요청에 최적화된 상태로 먼저 만들고 쿼리의 요청을 읽어들이는 방식.
# [s1, s2 , s3, s4, s5, s6] 와 같은 데이터가 있으면,
# [s1, s1+s2, s1+s2+s3, s1+s2+s3+s4 ,....] O(N)
# ex) 쿼리의 요청에 따라 s1+s2, s1을 불러오면 s2를 바로 알 수 있다. O(1)
# s1 + s2 + s3 + s4, s1 + s2 => s3 + s4를 바로 알 수 있다.

def solution2(S, P, Q):
    A, C, G, T = 0, 0, 0, 0
    cummulated = [(0, 0, 0, 0)]
    answer = []
    # S를 순회하며 ACGT가 몇 번 발현되었는지 저장
    for char in S:
        if char == 'A':
            A += 1
        elif char == 'C':
            C += 1
        elif char == 'G':
            G += 1
        elif char == 'T':
            T += 1

        cummulated.append((A, C, G, T))

    for p, q in zip(P, Q):
        left, right = cummulated[p], cummulated[q+1]
        if left[0] != right[0]:
            answer.append(1)
        elif left[1] != right[1]:
            answer.append(2)
        elif left[2] != right[2]:
            answer.append(3)
        elif left[3] != right[3]:
            answer.append(4)

    return answer

