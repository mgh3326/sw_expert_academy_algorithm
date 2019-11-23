import sys

sys.stdin = open("./data/sample_input (14).txt")


def find_borad():
    is_find = True
    for w in range(W):
        for h in range(D - K + 1):
            temp_value = board_list[h][w]
            is_find = True
            for i in range(K - 1):
                if temp_value != board_list[h + i + 1][w]:
                    is_find = False
                    break
            else:
                break

        if not is_find:
            return False
    if is_find:
        return True
    else:
        return False


def dfs(depth, start_idx):
    global is_end
    global result
    if depth == size:
        temp_list = []
        for current_idx, current_idx_color in idx_color_list:
            temp_list.append(board_list[current_idx].copy())
            board_list[current_idx] = color_list[current_idx_color]
        if find_borad():
            is_end = True
            result = size
            return
        idx = 0
        for current_idx, current_idx_color in idx_color_list:
            board_list[current_idx] = temp_list[idx]
            idx += 1
        return

    for idx in range(start_idx, D):
        for color in range(2):
            idx_color_list.append((idx, color))
            dfs(depth + 1, idx + 1)
            if is_end:
                return
            idx_color_list.pop()


T = int(input())
for test_case_idx in range(T):
    is_end = False
    D, W, K = map(int, input().split())
    color_list = []
    A_list = [0] * W
    B_list = [1] * W
    color_list.append(A_list)
    color_list.append(B_list)
    result = K
    board_list = [list(map(int, input().split())) for i in range(D)]
    for size in range(K):
        idx_color_list = []
        dfs(0, 0)
        if is_end:
            break
    print("#%d %d" % (test_case_idx + 1, result))
