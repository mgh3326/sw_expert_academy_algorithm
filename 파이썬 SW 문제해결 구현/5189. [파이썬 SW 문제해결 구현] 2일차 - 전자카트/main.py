import sys

sys.stdin = open("./sample_input.txt")


def dfs(depth):
    global current_value
    global result
    global depth_count
    if depth_count == m:
        if result == -1 or result > current_value + board_list[depth][0]:
            result = current_value + board_list[depth][0]
        return
    for current_w in range(m):
        if depth == current_w:
            continue
        if visit_w_list[current_w]:
            continue
        visit_w_list[current_w] = True
        current_value += board_list[depth][current_w]
        depth_count += 1
        dfs(current_w)
        depth_count -= 1
        current_value -= board_list[depth][current_w]
        visit_w_list[current_w] = False


test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = -1
    m = int(input())
    board_list = []
    for i in range(m):
        temp_list = list(map(int, input().split()))
        board_list.append(temp_list)
    visit_w_list = [False] * m
    visit_w_list[0] = True
    depth_count = 0
    depth_count += 1
    current_value = 0
    dfs(0)
    print("#%d %d" % (test_case_index + 1, result))
