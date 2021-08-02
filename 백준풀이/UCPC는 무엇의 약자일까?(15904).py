S = input()
UCPC = ['U', 'C', 'P', 'C']
idx = 0

for i in range(len(S)):
    if idx == 4:
        break

    if S[i] == UCPC[idx]:
        idx += 1

if idx == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')