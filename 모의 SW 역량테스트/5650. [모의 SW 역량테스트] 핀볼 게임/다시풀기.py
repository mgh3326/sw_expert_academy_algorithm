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

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    N = int(input())
    board_list = [[5] * (N + 2)]
    warm_hall_dict = {}
    for h in range(N):
        temp_list = [5]
        temp_list.extend(list(map(int, input().split())))
        for w in range(1, len(temp_list)):
            if temp_list[w] > 5:
                if temp_list[w] not in warm_hall_dict:
                    warm_hall_dict[temp_list[w]] = (h + 1, w)
                else:
                    warm_hall_dict[h + 1, w] = warm_hall_dict[temp_list[w]]
                    warm_hall_dict[warm_hall_dict[temp_list[w]]] = (h + 1, w)
                    warm_hall_dict.pop(temp_list[w])

        temp_list.append(5)
        board_list.append(temp_list)
    board_list.append([5] * (N + 2))
    for start_h in range(1, N + 1):
        for start_w in range(1, N + 1):
            if board_list[start_h][start_w] != 0:
                continue
            for current_dir in range(4):
                current_h, current_w = start_h, start_w
                score = 0
                count = 0
                while True:
                    if (count != 0 and start_h == current_h and start_w == current_w) or board_list[current_h][
                        current_w] == -1:  # 시작점으로 와버림 또는 블랙홀
                        break
                    if 1 <= board_list[current_h][current_w] <= 5:
                        current_dir = block_dict[board_list[current_h][current_w]][current_dir]
                        score += 1
                    elif board_list[current_h][current_w] > 5:
                        (current_h, current_w) = warm_hall_dict[current_h, current_w]
                    dh, dw = dir_list[current_dir]
                    current_h, current_w = dh + current_h, dw + current_w
                    count += 1
                if score > result:
                    result = score

    print("#%d %d" % (test_case_index + 1, result))
