# 문제풀이 :
#   이분탐색으로 접근.
#   start를 금액 리스트의 최대값, end를 금액 리스트의 총합으로 둔다
#   mid를 인출 금액으로 두고 인출 횟수를 계산한다.
#   계산된 횟수를 count 변수에 담아두고,
#   1) count 변수가 M보다 작은경우 가격을 올려야 하기 때문에 탐색 범위를 start = mid +1 (가격대를 높힘)한다.
#   2) count 변수가 M보다 크거나 같은 경우 가격을 낮춰야 하기 때문에 탐색 범위를 end = mid -1 한다.
#   가장 최소 금액을 구해야하기 때문에 answer에다가 최소 금액을 최신화 해서 출력하면 정답.
N, M = list(map(int,input().split()))
price_list = [int(input()) for _ in range(N)]
start = max(price_list)
end = sum(price_list)
answer = 9999999999999
while end - start >= 0:
    mid = (start + end) // 2
    count = 1
    reminder = mid
    for price in price_list:
        reminder -= price
        if reminder < 0:
            reminder = mid - price
            count += 1
    if M >= count:
        if answer > mid:
            answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)

