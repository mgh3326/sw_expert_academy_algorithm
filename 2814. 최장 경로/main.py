import sys

sys.stdin = open("./data/input.txt")

import math


def dfs(depth, current_idx):
    global result
    for value in my_list[current_idx]:
        if value in visit_set:
            continue
        visit_set.add(value)
        result = max(depth + 1, result)
        dfs(depth + 1, value)
        visit_set.remove(value)


T = int(input())
for test_case_idx in range(T):
    N, M = map(int, input().split())
    my_list = [list() for i in range(N)]
    for i in range(M):
        x, y = map(int, input().split())
        my_list[x - 1].append(y - 1)
        my_list[y - 1].append(x - 1)
    result = 1
    # for i in range(math.ceil(N / 2)): # 왜 math.ceil하면 예외가 존재할까?
    for i in range(math.ceil(N / 2)):
        visit_set = set()
        visit_set.add(i)
        dfs(1, i)
    print("#%d %d" % (test_case_idx + 1, result))
