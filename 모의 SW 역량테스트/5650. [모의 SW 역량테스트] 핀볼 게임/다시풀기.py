import sys

sys.stdin = open("./data/sample_input.txt")
# TODO 풀다 도망
block_dict = {
    1: [1, 3, 0, 2],
    2: [3, 0, 1, 2],
    3: [2, 0, 3, 1],
    4: [1, 2, 3, 0],
    5: [1, 0, 3, 2],
}
dir_list = [
    [-1, 0],  # 상
    [1, 0],  # 하
    [0, -1],  # 좌
    [0, 1],  # 우
]


def dfs(input_h, input_w, input_dir_idx, depth):
    global current_score
    global result
    if depth != 0 and (
            (input_h == start_h and input_w == start_w) or board_value_list[input_h][input_w] == -1):  # 종료
        if result < current_score:
            result = current_score
        return
    dh, dw = dir_list[input_dir_idx]
    nh = input_h + dh
    nw = input_w + dw
    if nh < 0 or nw < 0 or nh >= N or nw >= N:
        current_score += 1
        if board_value_list[input_h][input_w] == 0:
            if visit_list[input_h][input_w][block_dict[5][input_dir_idx]] >= current_score:
                return
            visit_list[input_h][input_w][block_dict[5][input_dir_idx]] = current_score
        if 1 <= board_value_list[input_h][input_w] <= 5:
            current_score += 1

            dfs(input_h, input_w, block_dict[board_value_list[input_h][input_w]][block_dict[5][input_dir_idx]],
                depth + 1)
        elif 5 < board_value_list[input_h][input_w]:  # 웜홀 일때
            warm_hall_h, warm_hall_w = warm_hall_dict[input_h, input_w]
            dfs(warm_hall_h, warm_hall_w, block_dict[5][input_dir_idx], depth + 1)
        else:
            dfs(input_h, input_w, block_dict[5][input_dir_idx], depth + 1)
        return
    elif 1 <= board_value_list[nh][nw] <= 5:
        current_score += 1
        # if board_value_list[input_h][input_w] == 0:
        #     if visit_list[input_h][input_w][block_dict[board_value_list[nh][nw]][input_dir_idx]] >= current_score:
        #         return
        #     visit_list[input_h][input_w][block_dict[board_value_list[nh][nw]][input_dir_idx]] = current_score
        dfs(nh, nw, block_dict[board_value_list[nh][nw]][input_dir_idx], depth + 1)
        return
    elif 5 < board_value_list[nh][nw]:  # 웜홀 일때
        warm_hall_h, warm_hall_w = warm_hall_dict[nh, nw]
        dfs(warm_hall_h, warm_hall_w, input_dir_idx, depth + 1)
        return
    elif (nh == start_h and nw == start_w) or board_value_list[nh][nw] == -1:  # 종료
        if result < current_score:
            result = current_score
        return
    elif board_value_list[nh][nw] == 0:
        # if visit_list[nh][nw][input_dir_idx] >= current_score:
        #     return
        # visit_list[nh][nw][input_dir_idx] = current_score
        dfs(nh, nw, input_dir_idx, depth + 1)
    return


test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    board_value_list = []
    visit_list = []
    warm_hall_dict = {}
    N = int(input())
    for h in range(N):
        temp_list = []
        temp_list.append(5)
        temp_list = list(map(int, input().split()))
        temp_visit_list = []
        for w in range(len(temp_list)):
            visit_value = []
            temp_value = temp_list[w]
            if temp_value == 0:
                visit_value = [-1] * len(dir_list)
            elif 6 <= temp_value <= 10:
                if temp_value in warm_hall_dict:
                    warm_hall_dict[h, w] = warm_hall_dict[temp_value]
                    warm_hall_dict[warm_hall_dict[temp_value]] = (h, w)
                    warm_hall_dict.pop(temp_value)
                else:
                    warm_hall_dict[temp_value] = (h, w)
            temp_visit_list.append(visit_value)
        visit_list.append(temp_visit_list)
        board_value_list.append(temp_list)
    for start_h in range(N):
        for start_w in range(N):
            if board_value_list[start_h][start_w] == 0:
                for dir_idx in range(len(dir_list)):
                    current_score = 0
                    if visit_list[start_h][start_w][dir_idx] >= current_score:
                        continue
                    visit_list[start_h][start_w][dir_idx] = current_score

                    dfs(start_h, start_w, dir_idx, 0)

    print("#%d %d" % (test_case_index + 1, result))
