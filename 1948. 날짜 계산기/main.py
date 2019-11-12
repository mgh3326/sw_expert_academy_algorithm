import sys

sys.stdin = open("./data/input.txt")

date_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
T = int(input())
for test_case_idx in range(T):
    result = 0
    start_month, start_day, end_month, end_day = map(int, input().split())
    for i in range(start_month, end_month):
        result += date_list[i]
    result -= start_day - 1
    result += end_day
    print("#%d %d" % (test_case_idx + 1, result))
