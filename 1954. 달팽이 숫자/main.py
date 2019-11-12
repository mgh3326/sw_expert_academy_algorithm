import sys

sys.stdin = open("./data/input.txt")
dir_list = [  # 우 하 좌 상
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
]
T = int(input())
for test_case_idx in range(T):
    N = int(input())
    board_list = [["" for _ in range(N)] for _ in range(N)]
    count = 0
    current_h, current_w = 0, 0
    current_dir_idx = 0
    while True:
        if count == N * N:
            break
        count += 1
        board_list[current_h][current_w] = str(count)
        dh, dw = dir_list[current_dir_idx]
        nh, nw = current_h + dh, current_w + dw
        if nh >= N or nw >= N or nh < 0 or nw < 0 or board_list[nh][nw] != "":
            current_dir_idx = (current_dir_idx + 1) % (len(dir_list))
            dh, dw = dir_list[current_dir_idx]
            nh, nw = current_h + dh, current_w + dw
        current_h, current_w = nh, nw
    print("#%d" % (test_case_idx + 1))
    for board in board_list:
        print(" ".join(board))
