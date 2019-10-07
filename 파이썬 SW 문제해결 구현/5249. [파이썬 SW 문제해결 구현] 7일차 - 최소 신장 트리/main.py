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
    start_index = 0
    visit_list = [False] * vertex_num
    while True:
        pass
    print("#%d %d" % (test_case_index + 1, result))
