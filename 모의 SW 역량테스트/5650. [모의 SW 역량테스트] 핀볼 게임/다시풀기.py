import sys

sys.stdin = open("./data/sample_input.txt")

dh = [-1, 1, 0, 0]  # 상 하 좌 우
dw = [0, 0, -1, 1]  # 상 하 좌 우


def dfs(input_h, input_w, score, depth, input_dir_idx):
    if depth != 0 and input_h == start_h and input_w == start_w:
        return


test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    board_value_list = []
    visit_list = []
    warm_hall_dict = {}
    n = int(input())
    for h in range(n):
        temp_list = list(map(int, input().split()))
        temp_visit_list = []
        for w in range(len(temp_list)):
            visit_value = []
            temp_value = temp_list[w]
            if temp_value == 0:
                visit_value = [-1] * len(dh)
            temp_visit_list.append(visit_value)
        visit_list.append(temp_visit_list)
        board_value_list.append(temp_list)
    for start_h in range(n):
        for start_w in range(n):
            if board_value_list[start_h][start_w] == 0:
                for dir_idx in range(len(dh)):
                    dfs(start_h, start_w, 0, 0, dir_idx)

    print("#%d %d" % (test_case_index + 1, result))
