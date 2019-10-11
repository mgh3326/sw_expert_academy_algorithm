import sys

sys.stdin = open("./input.txt")


class Node:
    def __init__(self):
        self.child = {}


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, input_str):
        node = self.root
        for current_str in input_str:
            if current_str not in node.child:
                _node = Node()
                node.child[current_str] = _node
            node = node.child[current_str]

    def find(self, input_str):
        node = self.root
        is_ok = True
        for current_str in input_str:
            if current_str not in node.child:
                is_ok = False
                break
            node = node.child[current_str]
        return is_ok

    def find_index_value(self, input_index):
        self.dfs(self.root, input_index)

    def dfs(self, node, input_index):
        global count
        global current_value
        keys = sorted(node.child.keys())
        parent_node = node
        for key in keys:
            node = node.child[key]
            current_value += key
            count += 1
            if count == input_index:
                return True
            if self.dfs(node, input_index):
                return True
            node = parent_node
            current_value = current_value[:-1]


test_case_num = int(input())
for test_case_index in range(test_case_num):
    current_value = ""
    count = 0
    n, temp_str = input().split()
    n = int(n)
    trie = Trie()
    for i in range(len(temp_str)):
        trie.insert(temp_str[i:])
    trie.find_index_value(n)
    print("#%d %s %d" % (test_case_index + 1, current_value[0], len(current_value)))
