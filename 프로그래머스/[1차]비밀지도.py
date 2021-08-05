def solution(n, arr1, arr2):
    answer = [[-1] * n for _ in range(n)]

    # 10진수 -> 2진수로 변환
    for i in range(n):
        arr1[i] = format(arr1[i], 'b').zfill(n)
        arr2[i] = format(arr2[i], 'b').zfill(n)

    # 2개의 배열 합치기(or 연산)
    for i in range(n):
        for j in range(len(answer[i])):
            if int(arr1[i][j]) or int(arr2[i][j]):
                answer[i][j] = '#'
            else:
                answer[i][j] = ' '

    ans = []
    for i in range(n):
        ans.append(''.join(answer[i]))

    return ans


'''
- 10진수 -> 2진수

format(10진수, 'b')


- 2진수 -> 10진수

int(2진수, 2)

- 문자열 타입에서 자릿수 채우기 
 .zfill(n) 원하는 자리수만큼 앞에 0을 채운다
 
 ex) a = '5'
 a.zfill(3) => 005


'''


