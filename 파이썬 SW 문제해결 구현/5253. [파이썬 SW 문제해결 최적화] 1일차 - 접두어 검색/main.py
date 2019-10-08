import sys

sys.stdin = open("./input.txt")


# TODO 클래스에서 self 있을때랑 딕셔너리 재사용이 달라진다
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


test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    n, m = map(int, input().split())
    trie = Trie()
    for i in range(n):
        temp_value = input()
        trie.insert(temp_value)
    for i in range(m):
        temp_value = input()
        if trie.find(temp_value):
            result += 1
    print("#%d %d" % (test_case_index + 1, result))
