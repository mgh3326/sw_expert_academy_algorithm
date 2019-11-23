import sys

sys.stdin = open("./data/input.txt")


def dfs(depth):
    global current_value
    global result
    if depth == N:
        if current_value == K:
            result += 1
        return
    dfs(depth + 1)
    current_value += board_list[depth]
    dfs(depth + 1)
    current_value -= board_list[depth]


T = int(input())
for test_case_idx in range(T):
    result = 0
    N, K = map(int, input().split())
    board_list = list(map(int, input().split()))
    current_value = 0
    dfs(0)
    print("#%d %d" % (test_case_idx + 1, result))
