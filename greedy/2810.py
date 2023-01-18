n = int(input())
member = input()

couple = member.count('LL')

if (couple <= 1):
    print(len(member))
else:
    print(len(member) - couple + 1)