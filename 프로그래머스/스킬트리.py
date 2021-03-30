# 브루트포스 알고리즘 활용
# 모든 스킬트리를 순회하면서 step이 맞는지 체크

def solution(skill, skill_trees):
    answer = 0
    li_skill = list(skill)
    for i in range(len(skill_trees)):
        step = 0
        value = True
        for j in skill_trees[i]:
            if j in li_skill:
                index = li_skill.index(j)
                if step < index:
                    value = False
                    break
                elif step == index:
                    step += 1
        if value:
            answer += 1

    return answer