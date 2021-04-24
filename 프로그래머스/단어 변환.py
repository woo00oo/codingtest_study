# 한 글자만 다른 단어 = 연결되어있는 노드

answer = 0


def dfs(begin, target, words, visited):
    # 전역 변수 answer를 사용하겠다고 설정.
    global answer
    stacks = [begin]

    while stacks:
        # 스택을 활용한 dfs 구현
        stack = stacks.pop()

        if stack == target:
            return answer

        for w in range(0, len(words)):
            # 조건 1. 한 개의 알파벳만 다른 경우
            # words에 있는 한개 한개의 단어가 이전 비교값과 스펠링이 1개만 다르다면 방문여부를 true(1)로 변경하고, stacks에 추가
            if len([i for i in range(0, len(words[w])) if words[w][i] != stack[i]]) == 1:

                if visited[w] != 0:
                    continue

                visited[w] = 1

                # stack에 추가
                stacks.append(words[w])

        # depth +
        answer += 1


def solution(begin, target, words):
    global answer

    # 조건 2. words에 있는 단어로만 변환할 수 있습니다.
    if target not in words:
        return 0

    #방문 여부를 words의 갯수만큼 0으로 초기화
    visited = [0 for i in words]


    dfs(begin, target, words, visited)

    return answer

print(solution('hit','dog',["hot", "dot", "dog", "lot", "log", "cog"]))