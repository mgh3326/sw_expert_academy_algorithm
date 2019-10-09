import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    n = int(input())
    board_list = []
    red_set = set()
    blue_set = set()
    for i in range(n):
        h_min, w_min, h_max, w_max, value = (map(int, input().split()))
        for h in range(h_min, h_max + 1):
            for w in range(w_min, w_max + 1):
                if value == 1:
                    red_set.add((h, w))
                else:
                    blue_set.add((h, w))
    intersection = red_set.intersection(blue_set)
    result = len(intersection)
    print("#%d %d" % (test_case_index + 1, result))
