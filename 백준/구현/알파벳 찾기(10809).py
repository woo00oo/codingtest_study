alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

S = input()

for i in range(len(alpha)):
    for j in range(len(S)):
        if alpha[i] == S[j]:
            alpha[i] = str(j)
    if alpha[i].isalpha():
        alpha[i] = -1

print(*alpha)