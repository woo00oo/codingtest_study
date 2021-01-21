word = input()
up_word = ''
answer = 'z' * 50

for i in range(1,len(word)):
    for j in range(len(word)-1,i,-1):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        up_word = a[::-1] + b[::-1] + c[::-1]
        if answer > up_word:
            answer = up_word

print(answer)

