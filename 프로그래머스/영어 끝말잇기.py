def solution(n, words):
    check = set()
    check.add(words[0])

    for i in range(1, len(words)):
        if words[i] in check or words[i-1][-1] != words[i][0]:
            number = (i + 1) % n
            if number == 0:
                number = n
            r = (i // n) + 1
            answer = [number, r]

            return answer

        check.add(words[i])

    return [0, 0]
