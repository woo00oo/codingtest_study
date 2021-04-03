# combinations(조합) 와 permutations(순열) 함수는 시간복잡도를 많이 차지 하기 때문에 항상 사용 전에 리스트의 최대 길이를 생각하고 사용하자.

# from itertools import combinations
#
# def solution(nums):
#     c = len(nums) // 2
#     li = list(combinations(nums,c))
#     answer = 0
#     for i in range(len(li)):
#         s = set(li[i])
#         if answer < len(s):
#             answer = len(s)
#
#     return answer

def solution(nums):
    c = len(nums) // 2
    Set = set(nums)
    if c >= len(Set):
        return len(Set)
    else:
        return c

print(solution([3,1,2,3]))