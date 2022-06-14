import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(Node)
    
    def insert(self, string):
        cur_node = self.head

        for s in string:
            if s not in cur_node.children:
                cur_node.children[s] = Node(s)
            cur_node = cur_node.children[s]
    
    def search_prefix(self, string):
        cur_node = self.head

        for s in string:
            cur_node = cur_node.children[s]
        
        if cur_node.children:
            return False
        else:
            return True

t = int(input())
for _ in range(t):
    n = int(input())
    trie = Trie()
    nums = []
    for _ in range(n):
        num = input().strip()
        nums.append(num)
        trie.insert(num)
    
    flag = True
    nums.sort()
    for num in nums:
        if not trie.search_prefix(num):
            flag = False
            break
    
    if flag:
        print("YES")
    else:
        print("NO")