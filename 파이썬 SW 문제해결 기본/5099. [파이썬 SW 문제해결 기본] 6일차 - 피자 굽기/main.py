import sys

sys.stdin = open("./input.txt")

# TODO 문제 이해 실패
test_case_num = int(input())

for test_case_index in range(test_case_num):
    result = 0
    n, m = map(int, input().split())
    board_list = list(map(int, input().split()))

    print("#%d %d" % (test_case_index + 1, result))
