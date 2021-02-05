#문제풀이 :
#   문자열 -> ASCII 코드 => ord()
#   ASCII코드 -> 문자열 => chr()
#   코드가 길다보니 실수하기가 쉽고, 어디서 실수를 했는지 찾기가 매우 어렵다!!
#   꼼꼼하게 코드를 작성..

K, S, N = input().split()

for _ in range(int(N)):
    k = ''
    k1 = ''
    s = ''
    s1 = ''
    i = input()
    if i == 'R' or i == 'L':
        k = ord(K[0])
        if i == 'R':
            k += 1
        else:
            k -= 1
        if 'A' <= chr(k) <= 'H':
            if chr(k) + K[1] == S:
                s = ord(S[0])
                if i == 'R':
                    s += 1
                else:
                    s -= 1
                if 'A' <= chr(s) <= 'H':
                    K = chr(k) + K[1]
                    S = chr(s) + S[1]
            else:
                K = chr(k) + K[1]
    elif i == 'B' or i == 'T':
        k = int(K[1])
        if i == 'B':
            k -= 1
        else:
            k += 1
        if 1 <= k <= 8:
            if K[0] + str(k) == S:
                s = int(S[1])
                if i == 'B':
                    s -= 1
                else:
                    s += 1
                if 1 <= s <= 8:
                    K = K[0] + str(k)
                    S = S[0] + str(s)
            else:
                K = K[0] + str(k)
    else:
        k = ord(K[0])
        k1 = int(K[1])
        if i == 'RT':
            k += 1
            k1 += 1
        elif i == 'LT':
            k -= 1
            k1 += 1
        elif i == 'RB':
            k += 1
            k1 -= 1
        else:
            k -= 1
            k1 -= 1
        if 'A' <= chr(k) <= 'H' and 1 <= k1 <= 8:
            if chr(k) + str(k1) == S:
                s = ord(S[0])
                s1 = int(S[1])
                if i == 'RT':
                    s += 1
                    s1 += 1
                elif i == 'LT':
                    s -= 1
                    s1 += 1
                elif i == 'RB':
                    s += 1
                    s1 -= 1
                else:
                    s -= 1
                    s1 -= 1
                if 'A' <= chr(s) <= 'H' and 1 <= s1 <= 8:
                    K = chr(k) + str(k1)
                    S = chr(s) + str(s1)
            else:
                K = chr(k) + str(k1)
print(K)
print(S)
