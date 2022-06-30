from collections import defaultdict

def solution(genres, plays):
    answer = []
    song = defaultdict(list)
    count = defaultdict(int)
    for i in range(len(genres)):
        song[genres[i]].append((plays[i], i))
        count[genres[i]] += plays[i] 
    
    count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    for gen, num in count:
        temp = 0
        play = sorted(song[gen], key=lambda x: (-x[0], x[1]))
        print(play)
        for amount, index in play:
            temp += 1
            if temp > 2:
                break
            answer.append(index)
    return answer