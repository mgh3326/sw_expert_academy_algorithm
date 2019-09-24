import sys

sys.stdin = open("./data/sample_input.txt")

dh = [-1, 1, 0, 0]  # 상하좌우
dw = [0, 0, -1, 1]  # 상하좌우
test_case_num = int(input())
for test_case_index in range(test_case_num):
    tunnel_height, tunnel_width, tunnel_start_h, tunnel_start_w, tunnel_l = map(int, input().split())
    tunnel_board_list = []
    for i in range(tunnel_height):
        temp_list = list(map(int, input().split()))
        tunnel_board_list.append(temp_list)
    tunnel_dict = {
        0: [],
        1: [0, 1, 2, 3],
        2: [0, 1],
        3: [2, 3],
        4: [0, 3],
        5: [1, 3],
        6: [1, 2],
        7: [0, 2],
    }
    tunnel_set = set()
    if tunnel_board_list[tunnel_start_h][tunnel_start_w] != 0:
        tunnel_set.add((tunnel_start_h, tunnel_start_w))
    queue = []
    queue.append([tunnel_start_h, tunnel_start_w, 1])
    while True:
        if len(queue) == 0:
            break
        current_h, current_w, depth = queue.pop(0)
        if depth == tunnel_l:  # TODO BFS 일때 queue에 담기 이전에 조건이 충족되면 끝내는 것을 고려해주어야한다.
            continue
        for dir_idx in tunnel_dict[(tunnel_board_list[current_h][current_w])]:
            next_h = current_h + dh[dir_idx]
            next_w = current_w + dw[dir_idx]
            if next_h < 0 or next_w < 0 or next_h >= tunnel_height or next_w >= tunnel_width:
                continue
            find_idx = dir_idx
            if dir_idx % 2 == 0:
                find_idx += 1
            else:
                find_idx -= 1
            if find_idx not in tunnel_dict[tunnel_board_list[next_h][next_w]]:
                continue
            if (next_h, next_w) in tunnel_set:
                continue
            tunnel_set.add((next_h, next_w))
            if depth + 1 >= tunnel_l:
                continue
            queue.append([next_h, next_w, depth + 1])

    result = len(tunnel_set)
    print("#%d %d" % (test_case_index + 1, result))
