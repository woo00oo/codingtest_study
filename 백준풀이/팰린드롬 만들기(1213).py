# ord : 특정한 한 문자를 아스키 코드 값으로 변환해 주는 함수
# chr : 아스키 코드 값을 문자로 변화해주는 함수


# 문자열을 S에 입력받고 S_cnt에 S 에 포함된 알파벳 대문자 수를 저장한다
S = input()
S_cnt = [0 for _ in range(26)]
for s in S:
    S_cnt[ord(s)-65] += 1

# for문을 돌면서 홀수인 알파벳 대문자가 몇 개 있는지 확인하고 홀수 알파벳과 짝수 알파벳을 저장한다.
odd = 0
odd_alpha = ''
alpha = ''

for i in range(26):
    if S_cnt[i] % 2 == 1:
        odd += 1
        odd_alpha += chr(i+65)
    alpha += chr(i+65) * (S_cnt[i] // 2)

# 홀수가 2개 이상이라면 팰린드롬을 만들 수 없다
if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(alpha+odd_alpha+alpha[::-1])