import sys

sys.stdin = open("./data/sample_input.txt")


def dfs(depth, current_h, current_w):
    global result
    result = max(result, depth)
    for dh, dw in dir_list:
        nh, nw = current_h + dh, current_w + dw
        if nh >= N or nw >= N or nh < 0 or nw < 0:
            continue
        if board_list[nh][nw] >= board_list[current_h][current_w]:
            continue
        if visit_list[nh][nw] >= depth:
            continue
        visit_list[nh][nw] = depth
        dfs(depth + 1, nh, nw)


dir_list = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]

T = int(input())
for test_case_idx in range(1, T + 1):
    N, K = map(int, input().split())
    board_list = [list(map(int, input().split())) for i in range(N)]
    peak_list = []
    result = 1
    max_value = 1
    for h in range(N):
        max_value = max(max_value, max(board_list[h]))
    for h in range(N):
        for w in range(N):
            if board_list[h][w] == max_value:
                peak_list.append((h, w))
    for h in range(N):
        for w in range(N):
            for peak_h, peak_w in peak_list:
                if peak_h == h and peak_w == w:
                    continue
                for k in range(1, K + 1):
                    visit_list = [[-1 for i in range(N)] for j in range(N)]
                    visit_list[h][w] = 0
                    board_list[h][w] -= k
                    dfs(1, peak_h, peak_w)
                    board_list[h][w] += k
    print("#%d %d" % (test_case_idx, result))
