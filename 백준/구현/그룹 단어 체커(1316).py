N = int(input())
li = [input() for _ in range(N)]
cnt = 0
for word in li:
    group = list()
    group_word = True
    for i in range(len(word)):
        if word[i] not in group:
            group.append(word[i])
        else:
            if word[i] == word[i-1]:
                continue
            else:
                group_word = False
                break
    if group_word:
        cnt += 1

print(cnt)