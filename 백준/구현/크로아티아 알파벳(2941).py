# 내가 푼 풀이:
#   크로아티아 알파벳이 반복해서 나오는 경우에는 원하는 답을 찾지 못하였다.
#   주어진 테스트케이스 경우를 모두 보아 예외 경우까지 생각해서 풀어나가자.
Alphabet = input()
answer = 0
N = len(Alphabet)
li = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=', 'dz=']
for i in range(8):
    if i == 7 and li[i] in Alphabet:
        answer += 1
        N -= 3
        break

    if li[i] in Alphabet:
        answer += 1
        N -= 2

print(answer + N)

# 참고 풀이:
#   replace(t,'*') 메소드는 문자열에서 해당 t를 모두 찾아 '8'로 바꾸어준다

a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpha = input()
for t in a:
    alpha = alpha.replace(t, '*')
print(len(alpha))

