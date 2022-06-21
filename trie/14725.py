import sys
input = sys.stdin.readline

class Trie(object):
    def __init__(self):
        self.head = {}

    def insert(self, array):
        cur_node = self.head

        for word in array:
            if word not in cur_node:
                cur_node[word] = {}
            cur_node = cur_node[word]
        cur_node["root"] = True
    
    def search(self, array, level):
        if "root" in array:
            return
        
        sorted_array = sorted(array)
        for word in sorted_array:
            print("--"*level + word)
            self.search(array[word], level + 1)
    
trie = Trie()
n = int(input())
for _ in range(n):
    array = list(map(str, input().split()))
    trie.insert(array[1:])

trie.search(trie.head, 0)