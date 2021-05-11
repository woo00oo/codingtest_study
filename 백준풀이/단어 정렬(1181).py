# (단어수, 단어) 형식으로 set에다가 저장
# set -> 리스트로 변환 후 lambda x : (x[1],x[0]) 로 길이가 짧은 것부터 길이가 같으면 사전순으로 정렬


N = int(input())
words = set()
for _ in range(N):
    word = input()
    word_len = len(word)
    words.add((word, word_len))

words_arr = list(words)
words_arr.sort(key=lambda x: (x[1], x[0]))

for word in words_arr:
    print(word[0])