import math

def solution(character, monsters):
    answer = ''
    
    war_list = []
    
    # 플레이어 입력 [체력, 공격력, 방어력]
    split_char = character.split()
    player = [int(split_char[0]), int(split_char[1]), int(split_char[2])]
    
    # 몬스터 입력 [이름, 경험치, 체력, 공격력, 방어력]
    monster_list = [[] for _ in range(len(monsters))]
    
    # 1초당 획득 경험치
    max_value = 0
    for j in range(len(monsters)):
        split_j = monsters[j].split()
        # [이름, 경험치, 체력, 공격력, 방어력]
        monster_list[j] = [split_j[0], int(split_j[1]), int(split_j[2]),
                           int(split_j[3]), int(split_j[4])]
        # 전투 진행
        # 초
        second = 0
        # 플레이어가 몬스터 공격했을 때 방어력이 더 큰 경우 나감
        if player[1] <= monster_list[j][4]:
            history = [monster_list[j][0], -1, 0, 0]
            war_list.append(history)
        # 플공 > 몬방이고 
        else:
            # 몬스터가 잃을 체력
            lose_weight = player[1] - monster_list[j][4]
            
            # 몬스터가 공격하기 전에 몬스터가 죽는다면
            if lose_weight >= monster_list[j][2]:
                history = [monster_list[j][0], 1, monster_list[j][1], monster_list[j][1]]
                war_list.append(history)
                if history[3] > max_value:
                    max_value = history[3]
            # 죽지 않는다면
            else:
                # 몬공-플방의 크기가 플레이어의 체력보다 크지 않다면 잡을 수 있음
                if (monster_list[j][3]-player[2]) <= player[0]:
                    # 걸리는 시간
                    second = math.ceil(monster_list[j][2] / lose_weight)
                    history = [monster_list[j][0], second, monster_list[j][1], monster_list[j][1]/second]
                    war_list.append(history)
                    if history[3] > max_value:
                        max_value = history[3]
                
                # 몬공-플방의 크기가 플체보다 크면 나감
                else:
                    history = [monster_list[j][0], -1, 0, 0]
                    war_list.append(history)
    
    # 몬스터 이름 리스트
    name_list = []
    for i in war_list:
        if i[3] == max_value:
            name_list.append(i[0])
    
    if len(name_list) > 1:
        max_ = 0
        for j in war_list:
            if j[2] > max_:
                max_ = j[2]
        for k in war_list:
            if k[2] == max_:
                answer = k[0]
                break
    else:
        answer = name_list[0]
    
    return answer

cha = "10 5 2"
mon = ["Knight 3 10 10 3","Wizard 5 10 15 1","Beginner 1 1 15 1"]

print(solution(cha, mon))