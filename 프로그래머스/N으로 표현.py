# 1. 주어진 숫자 N으로 각 횟수당 만들수 있는 숫자 조합을 만든다.
# 2. 만들어진 숫자 조합에 number로 주어진 숫자가 있는지 확인한다.
# 3. 만약 있다면 그 시점에서의 횟수를 답으로 리턴한다.
# 4. 없다면 횟수를 하나 늘리고 가능한 숫자 조합을 만들고 1~3번을 반복.

# N의 사용 횟수에 따라 만들어 낼 수 있는 숫자가 어떤게 있는지 확인.
# 사용 횟수가 1일때 숫자 5로 만들 수 있는 수 => 5
# 사용 횟수가 2일때 숫자 5로 만들 수 있는 수 => 55, 5+5, 5-5, 5*5, 5//5
# 사용 횟수가 3일때 숫자 5로 만들 수 있는 수 =? 555, (5+5) + 5 , (5+5) - 5, (5+5) *5 .....
# 패턴 -> N이 2인 숫자 조합을 만들기 위해서는 N이 1일때 경우의 수와 N이 1일때 경우의 수를 각각 사칙연산 진행
# N이 3인 숫자 조합을 만들기 위해서는 N이 2일때 경우의 수와 N이 1일때 경우의 수를 각각 사칙 연산 진행
# 즉, 특정 숫자만큼 5를 사용한 조합을 만들고 싶다면, 해당 숫자를 만들 수 있는 덧셈 조합의 경우의 수끼리 사칙연산을 해줌.

def solution(N, number):
    dp = [0,[N]] # 조합으로 나올수 있는 가능한 숫자들, 여기에 계속 append하며 이후에 사용함
    if N == number: #주어진 숫자와 사용해야 하는 숫자가 같은 경우는 1개면 족하므로 1으로 놓는다.
        return 1
    for i in range(2, 9): # 2부터 8까지로 횟수를 늘려 간다.
        case_set = [] # 임시로 사용할 케이스 셋, 각 I 별로 셋을 만들어 possible set에 붙인다.

        basic_num = int(str(N)*i) # 같은 숫자 반복되는 거 하나를 추가한다.
        case_set.append(basic_num)

        for i_half in range(1, i//2+1): # 사용되는 숫자의 횟수를 구해야 하는데, 절반 이상으로 넘어가면 같은 결과만 나올 뿐이므로 절반까지만을 사용한다.
            for x in dp[i_half]:
                for y in dp[i-i_half]: # x와 y를 더하면 i 가 되도록 만든 수다.
                    case_set.append(x+y)# 각 사칙연산 결과를 더한다.
                    case_set.append(x-y)
                    case_set.append(y-x)
                    case_set.append(x*y)
                    if y != 0:
                        case_set.append(x/y)
                    if x != 0:
                        case_set.append(y/x)
            # 해당 number가 case_set에 있을 경우
            if number in case_set:
                return i
            dp.append(case_set) # 최종 결과물 set에 사칙 연산 결과를 더한다.
    return -1 #N 이 8까지 답이 없으면 -1을 출력한다.