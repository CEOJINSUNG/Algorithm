import sys
input = sys.stdin.readline

class Trie(object):
    def __init__(self):
        self.root = {}
    
    def insert(self, array):
        cur_node = self.root

        for word in array:
            if word not in cur_node:
                cur_node[word] = {}
            cur_node = cur_node[word]
    
    def search(self, array, level):
        sorted_array = sorted(array)

        for word in sorted_array:
            print(" "*level + word)
            self.search(array[word], level+1)

trie = Trie()
n = int(input())
for _ in range(n):
    array = list(map(str, input().rstrip().split('\\')))
    trie.insert(array)

trie.search(trie.root, 0)