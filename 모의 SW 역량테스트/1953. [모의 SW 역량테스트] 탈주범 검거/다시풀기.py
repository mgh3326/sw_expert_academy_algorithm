import sys

sys.stdin = open("./data/sample_input.txt")
dir_list = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]
terrel_dict = {
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [0, 3],
    5: [1, 3],
    6: [1, 2],
    7: [0, 2],
}
inverse_dir_idx = [
    1, 0, 3, 2
]
T = int(input())
for test_case_idx in range(T):
    N, M, R, C, L = map(int, input().split())
    board_list = [list(map(int, input().split())) for i in range(N)]
    visit_list = [[False for _ in range(M)] for _ in range(N)]
    result = 1
    queue = [[R, C, 0]]
    visit_list[R][C] = True
    queue_idx = 0
    while True:
        if queue_idx >= len(queue) >= 0:
            break
        h, w, cost = queue[queue_idx]
        for dir_idx in terrel_dict[board_list[h][w]]:
            dh, dw = dir_list[dir_idx]
            nh, nw = h + dh, w + dw
            if nh >= N or nw >= M or nh < 0 or nw < 0 or board_list[nh][nw] == 0 or visit_list[nh][nw] is True:
                continue
            if inverse_dir_idx[dir_idx] not in terrel_dict[board_list[nh][nw]]:
                continue
            if cost + 1 == L:
                continue
            visit_list[nh][nw] = True
            result += 1
            queue.append([nh, nw, cost + 1])
        queue_idx += 1

    print("#%d %d" % (test_case_idx + 1, result))
