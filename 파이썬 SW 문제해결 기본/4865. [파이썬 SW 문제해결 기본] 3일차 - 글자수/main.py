import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    find_str = input()
    total_str = input()
    find_dict = {}
    total_dict = {}
    for i in find_str:
        if i not in find_dict:
            find_dict[i] = 0
        find_dict[i] += 1
    for i in total_str:
        if i not in total_dict:
            total_dict[i] = 0
        total_dict[i] += 1
    for find_dict_key in find_dict.keys():
        if find_dict_key in total_dict:
            if result < total_dict[find_dict_key]:
                result = total_dict[find_dict_key]
    print("#%d %s" % (test_case_index + 1, result))
