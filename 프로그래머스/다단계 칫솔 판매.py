# 하나의 노드로 부터 부모를 타고 올라가 루트까지 도달하는 문제.
# 10%를 계산한 금액이 1원 미만인 경우에는 이득을 분배하지 않고 자신이 모두 가지기 때문에 break를 걸어줘야 시간초과가 발생하지 않는다.

def solution(enroll, referral, seller, amount):
    tree = {'-': 'root'}
    sell_price = {'-': 0}

    # 트리 생성
    for i in range(len(enroll)):
        child = enroll[i]
        parent = referral[i]
        sell_price[child] = 0
        tree[child] = parent

    #
    for i in range(len(seller)):
        child = seller[i]
        parent = tree[child]
        money = amount[i] * 100
        sell_price[child] += money

        while True:
            commission = money // 10
            sell_price[child] -= commission
            sell_price[parent] += commission

            if commission == 0:
                break

            child = parent
            parent = tree[child]
            money = commission

            if parent == 'root':
                break

    answer = []
    for person in enroll:
        answer.append(sell_price[person])

    return answer