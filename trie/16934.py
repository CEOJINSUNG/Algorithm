from collections import defaultdict
import sys
input = sys.stdin.readline

class Node():
    def __init__(self):
        self.exist = False
        self.children = {}

class Trie():
    def __init__(self):
        self.root = Node()
    
    def insert(self, string):
        cur_node = self.root

        for s in string:
            if s not in cur_node.children:
                cur_node.children[s] = Node()
            cur_node = cur_node.children[s]
        cur_node.exist = True
    
    def search(self, string):
        cur_node = self.root
        prefix = ""
        for c in string:
            prefix += c
            if c not in cur_node.children:
                return prefix
            cur_node = cur_node.children[c]
        
        if cur_node.exist:
            prefix += str(check[prefix] + 1)
        return prefix
        

trie = Trie()
n = int(input())
check = defaultdict(int)
for _ in range(n):
    word = input().rstrip()
    print(trie.search(word))
    check[word] += 1
    trie.insert(word)