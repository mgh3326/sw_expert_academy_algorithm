import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    n, m = map(int, input().split())
    board_list = list(map(int, input().split()))
    for i in range(m):
        pop = board_list.pop(0)
        board_list.append(pop)
    result = board_list[0]
    print("#%d %s" % (test_case_index + 1, result))
