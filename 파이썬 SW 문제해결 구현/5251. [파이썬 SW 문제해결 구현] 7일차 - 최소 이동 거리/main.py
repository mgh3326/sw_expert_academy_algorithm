import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    vertex_num, edge_num = map(int, input().split())
    vertex_num += 1
    board_list = []
    for i in range(vertex_num):
        board_list.append([0] * vertex_num)
    for i in range(edge_num):
        start, end, value = (map(int, input().split()))
        board_list[start][end] = value
        board_list[end][start] = value
    start_index = 0
    visit_list = [False] * vertex_num
    value_list = [-1] * vertex_num
    visit_list[start_index] = True
    value_list[start_index] = 0
    current_index = start_index
    current_value = 0
    while True:
        if current_index == vertex_num - 1:
            break
        for idx, board in enumerate(board_list[current_index]):
            if board != 0 and (value_list[idx] == -1 or value_list[idx] > board + current_value):
                value_list[idx] = board + current_value
        temp_min_value = -1
        temp_min_idx = 0
        for idx, value in enumerate(value_list):
            if visit_list[idx] is False and value_list[idx] != -1:
                if temp_min_value == -1 or temp_min_value > value_list[idx]:
                    temp_min_value = value_list[idx]
                    temp_min_idx = idx
        current_value += temp_min_value
        current_index = temp_min_idx
        visit_list[current_index] = True
    result = value_list[-1]
    print("#%d %d" % (test_case_index + 1, result))
