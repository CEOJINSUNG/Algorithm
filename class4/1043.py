import sys
input = sys.stdin.readline

N, M = map(int, input().split())
truth = list(map(int, input().split()))
party = []

if truth[0] == 0:
    for _ in range(M):
        non_use = list(map(int, input().split()))
    print(M)
elif truth[0] > 0:
    truth_participant = set(truth[1:])

    for _ in range(M):
        set_participant = set(list(map(int, input().split()))[1:])
        party.append(set_participant)

    for _ in range(M):
        for i, party_ in enumerate(party):
            if truth_participant.intersection(party_):
                truth_participant = truth_participant.union(party_)
    
    print(len([i for i in party if not truth_participant.intersection(i)]))