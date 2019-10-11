import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())
for test_case_index in range(test_case_num):
    e, n = map(int, input().split())
    tree = []
    for i in range(e + 2):
        tree.append([0] * 2)
    value_list = list(map(int, input().split()))
    for value_idx in range(len(value_list) // 2):
        parent, child = value_list[value_idx * 2], value_list[value_idx * 2 + 1]
        for i in range(2):
            if tree[parent][i] == 0:
                tree[parent][i] = child
                break
    result = 1
    queue = []
    queue_idx = 0
    queue.append(n)
    while True:
        if queue_idx >= len(queue):
            break
        value = queue[queue_idx]
        for i in tree[value]:
            if i == 0:
                break
            queue.append(i)
            result += 1
        queue_idx += 1
    print("#%d %s" % (test_case_index + 1, result))
