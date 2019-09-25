import sys

sys.stdin = open("./data/sample_input.txt")

dh = [-1, 1, 0, 0]  # 상 하 좌 우
dw = [0, 0, -1, 1]  # 상 하 좌 우


def bomb(input_h, input_w, input_remove_dict, input_w_list):
    temp_value = board_list[input_h][input_w]
    if temp_value not in input_remove_dict:
        input_remove_dict[temp_value] = []
    input_remove_dict[temp_value].append((input_h, input_w))
    board_list[input_h][input_w] = 0
    if temp_value != 0:
        if input_w not in input_w_list:
            input_w_list.append(input_w)
    for dir_idx in range(len(dh)):
        current_h, current_w = input_h, input_w
        for i in range(temp_value - 1):
            current_h += dh[dir_idx]
            current_w += dw[dir_idx]
            if current_h < 0 or current_w < 0 or current_h >= height or current_w >= width:
                break
            if board_list[current_h][current_w] != 0:
                bomb(current_h, current_w, input_remove_dict, input_w_list)


def dfs(depth):
    global current_count
    global result
    if depth == n + 1:
        return
    for w in range(width):
        remove_dict = {}
        w_list = []
        # 부시기
        # 1. 구슬 떨어뜨려서 맞는 지점 찾기
        h = 0
        while True:
            if h == height:
                break
            if board_list[h][w] != 0:
                bomb(h, w, remove_dict, w_list)
                break
            h += 1
        # TODO 내리기 부분이 꽤 삐리한것 같다
        down_dict = {}
        current_h = height - 1
        for _w in w_list:
            if _w == w:
                continue
            while True:
                if current_h < 0:
                    break
                if board_list[current_h][_w] == 0:
                    temp_h = current_h - 1
                    while True:
                        if temp_h < 0:
                            break
                        temp_value = board_list[temp_h][_w]
                        if temp_value != 0:
                            board_list[current_h][_w] = temp_value
                            board_list[temp_h][_w] = 0
                            if temp_value not in down_dict:
                                down_dict[temp_value] = []
                            down_dict[temp_value].append((temp_h, _w))
                            break
                        temp_h -= 1
                current_h -= 1
        current_count += len(remove_dict.values())
        if current_count > result:
            result = current_count
        dfs(depth + 1)
        for remove_dict_key in remove_dict.keys():
            for remove_dict_value in remove_dict[remove_dict_key]:
                h, w = remove_dict_value
                board_list[h][w] = remove_dict_key
                current_count -= 1
        for down_dict_key in down_dict.keys():
            for down_dict_value in down_dict[down_dict_key]:
                h, w = down_dict_value
                board_list[h][w] = down_dict_key

        # 복원하기


test_case_num = int(input())
for test_case_index in range(test_case_num):
    current_count = 0
    result = 0
    n, width, height = map(int, input().split())
    board_list = []
    for _h in range(height):
        temp_list = list(map(int, input().split()))
        board_list.append(temp_list)
    dfs(0)
    print("#%d %d" % (test_case_index + 1, result))
