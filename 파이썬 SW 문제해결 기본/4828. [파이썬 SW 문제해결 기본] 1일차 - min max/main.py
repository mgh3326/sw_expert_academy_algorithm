import sys

sys.stdin = open("./input.txt")


test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    n = int(input())
    board_list = list(map(int, input().split()))
    print("#%d %d" % (test_case_index + 1, max(board_list) - min(board_list)))
