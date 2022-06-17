from collections import defaultdict

def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for start, arrive in tickets:
        graph[start].append(arrive)
    
    for key in graph.keys():
        graph[key].sort(reverse=True)
    
    stack = ["ICN"]
    while stack:
        temp = stack[-1]
        
        if not graph[temp]:
            answer.append(stack.pop())
        else:
            stack.append(graph[temp].pop())
    
    answer.reverse()
    return answer