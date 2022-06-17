def solution(record):
    uid_nick_matching = {}
    answer = []
    for i in record:
        store = list(i.split())
        if store[0] == "Leave":
            continue
        else:
            uid = store[1]
            nick = store[2]
            uid_nick_matching[uid] = nick
    
    for j in record:
        command = list(j.split( ))[0]
        uid = list(j.split( ))[1]
        if command == "Enter":
            answer.append("{0}님이 들어왔습니다.".format(uid_nick_matching[uid]))
        elif command == "Leave":
            answer.append("{0}님이 나갔습니다.".format(uid_nick_matching[uid]))
    
    return answer

case = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(case)