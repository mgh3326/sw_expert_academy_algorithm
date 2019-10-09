import sys

sys.stdin = open("./input.txt")


def gravitation(m1, m2, d):
    return m1 * m2 / (d * d)


test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    n = int(input())
    board_list = list(map(int, input().split()))
    my_dict = {}
    for i in range(n):
        my_dict[board_list[i]] = board_list[i + n]
    my_dict_keys = sorted(my_dict.keys())
    for i in range(len(my_dict_keys))[1:]:
        distance
        for my_dict_key in my_dict_keys[:i]:
            pass
        for my_dict_key in my_dict_keys[i:]:
            pass
    print("#%d %d" % (test_case_index + 1, result))
