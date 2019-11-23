import sys

sys.stdin = open("./data/input.txt")

dir_list = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
    [-1, -1],
    [-1, 1],
    [1, -1],
    [1, 1],
]


def dfs(depth):
    global result
    if depth == N:
        result += 1
        return
    for i in range(N):
        current_h, current_w = depth, i
        if board_list[current_h][current_w] != 0:
            continue
        for dh, dw in dir_list:
            nh, nw = current_h, current_w
            while True:
                nh, nw = dh + nh, dw + nw
                if nh >= N or nw >= N or nh < 0 or nw < 0:
                    break
                board_list[nh][nw] += 1
        dfs(depth + 1)
        for dh, dw in dir_list:
            nh, nw = current_h, current_w
            while True:
                nh, nw = dh + nh, dw + nw
                if nh >= N or nw >= N or nh < 0 or nw < 0:
                    break
                board_list[nh][nw] -= 1


T = int(input())
for test_case_idx in range(T):
    result = 0
    N = int(input())
    board_list = [[0 for _ in range(N)] for _ in range(N)]
    dfs(0)
    print("#%d %d" % (test_case_idx + 1, result))
