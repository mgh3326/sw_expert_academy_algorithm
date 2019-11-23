import sys

sys.stdin = open("data/sample_input.txt")
dir_list = [
    [1, 1],
    [1, -1],
    [-1, -1],
    [-1, 1],
]
T = int(input())
for test_case_idx in range(T):
    result = -1
    N = int(input())
    board_list = [list(map(int, input().split())) for i in range(N)]
    for start_h in range(N):
        for start_w in range(N):
            for h_size in range(1, N):

                dh, dw = dir_list[0]
                current_h, current_w = start_h + dh * h_size, start_w + dw * h_size
                if current_h >= N or current_w >= N or current_h < 0 or current_w < 0:
                    break
                for w_size in range(1, N):
                    dh, dw = dir_list[1]
                    h, w = current_h + dh * w_size, current_w + dw * w_size
                    if h >= N or w >= N or h < 0 or w < 0:
                        break
                    dh, dw = dir_list[2]
                    h, w = h + dh * h_size, w + dw * h_size
                    if h >= N or w >= N or h < 0 or w < 0:
                        break
                    if h_size * 2 + w_size * 2 <= result:
                        continue
                    h, w = start_h, start_w
                    save_set = set()
                    for dir_idx in range(len(dir_list)):
                        size = 0
                        if dir_idx % 2 == 0:
                            size = h_size
                        else:
                            size = w_size
                        dh, dw = dir_list[dir_idx]
                        for idx in range(size):
                            h, w = dh + h, dw + w
                            if h >= N or w >= N or h < 0 or w < 0:
                                break
                            if board_list[h][w] in save_set:
                                break
                            save_set.add(board_list[h][w])
                            size -= 1
                        if size!=0:
                            break
                    if len(save_set) == h_size * 2 + w_size * 2:
                        result = max(result, len(save_set))
    print("#%d %d" % (test_case_idx + 1, result))
