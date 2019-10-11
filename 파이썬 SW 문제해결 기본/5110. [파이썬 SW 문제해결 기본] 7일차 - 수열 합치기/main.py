import sys

sys.stdin = open("./input.txt")


class Node:

    def __init__(self):
        self.next = None
        self.previous = None
        self.value = None


class LinkList:

    def __init__(self):
        self.root = Node()
        self.leaf = Node()

    def insert(self, input_list):
        node = self.root
        while True:
            if node.next is None:
                for i in range(len(input_list)):
                    node.next = Node()
                    value = input_list[i]
                    node.next.value = value
                    node.next.previous = node
                    node = node.next
                self.leaf.previous = node
                break
            elif node.next.value > input_list[0]:
                node_next = node.next
                for i in range(len(input_list)):
                    node.next = Node()
                    value = input_list[i]
                    node.next.value = value
                    node.next.previous = node
                    node = node.next
                node.next = node_next
                node_next.previous = node
                break

            node = node.next

    def print(self, length, reverse=True):
        node = self.leaf
        _result_list = []
        for i in range(length):
            _result_list.append(str(node.previous.value))
            node = node.previous
        return _result_list


def merge(input_list):
    global my_list
    for i in range(len(my_list)):
        if my_list[i] > input_list[0]:
            input_list.extend(my_list[i:])

            my_list = my_list[:i]
            my_list.extend(input_list)
            break
    else:
        my_list.extend(input_list)


test_case_num = int(input())
for test_case_index in range(test_case_num):
    is_end = False
    result = 0
    n, m = map(int, input().split())
    link_list = LinkList()
    for _ in range(m):
        temp_list = list(map(int, input().split()))
        link_list.insert(temp_list)

    result_list = link_list.print(10)
    result = str.join(" ", result_list)
    print("#%d %s" % (test_case_index + 1, result))
