from collections import defaultdict

def solution(skill, skill_trees):
    answer = 0
    category = defaultdict(int)
    
    for i in range(len(skill)):
        category[skill[i]] = i + 1
    
    for element in skill_trees:
        found = 1
        possible = True
        for char in element:
            if char in category.keys():
                if category[char] == found:
                    found += 1
                else:
                    possible = False
                    break
        if possible:
            answer += 1
    
    return answer