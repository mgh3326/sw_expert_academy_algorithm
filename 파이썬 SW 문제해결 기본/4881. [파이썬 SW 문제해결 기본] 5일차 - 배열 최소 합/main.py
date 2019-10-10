import sys

sys.stdin = open("./input.txt")


def dfs(depth):
    global result
    global current_value
    if current_value > result:  # 백트래킹
        return
    if depth == n:
        if current_value < result:
            result = current_value
        return
    for i in range(n):
        if not visit[i]:
            visit[i] = True
            current_value += board_list[depth][i]
            dfs(depth + 1)
            current_value -= board_list[depth][i]
            visit[i] = False


test_case_num = int(input())
for test_case_index in range(test_case_num):
    current_value = 0
    result = 0
    n = int(input())
    visit = [False] * n
    board_list = []
    for _ in range(n):
        temp_list = list(map(int, input().split()))
        result += temp_list[0]
        board_list.append(temp_list)
    dfs(0)
    print("#%d %s" % (test_case_index + 1, result))
