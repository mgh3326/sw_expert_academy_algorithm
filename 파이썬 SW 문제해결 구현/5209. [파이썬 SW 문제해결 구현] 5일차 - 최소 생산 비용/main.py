import sys

sys.stdin = open("./input.txt")


def dfs(depth):
    global result
    global current_value
    if depth == n:
        if result == -1 or result > current_value:
            result = current_value
            return
    if result != -1 and result <= current_value:
        return
    for w in range(n):
        if visit_list[w]:
            continue
        visit_list[w] = True
        current_value += board_list[depth][w]
        dfs(depth + 1)
        visit_list[w] = False
        current_value -= board_list[depth][w]


test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = -1
    n = int(input())
    board_list = []
    for i in range(n):
        temp_list = list(map(int, input().split()))
        board_list.append(temp_list)
    visit_list = [False] * n
    current_value = 0
    dfs(0)
    print("#%d %d" % (test_case_index + 1, result))
