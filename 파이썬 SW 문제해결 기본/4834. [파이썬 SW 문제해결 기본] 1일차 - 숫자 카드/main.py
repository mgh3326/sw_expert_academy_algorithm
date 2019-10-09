import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    n = int(input())
    number_dict = {}
    number_str = input()
    for i in number_str:
        if i not in number_dict:
            number_dict[i] = 0

        number_dict[i] += 1
    max_num = 0
    max_count = 0
    for number_dict_key in sorted(number_dict.keys(), reverse=True):
        if max_count < number_dict[number_dict_key]:
            max_count = number_dict[number_dict_key]
            max_num = number_dict_key

    print("#%d %s %d" % (test_case_index + 1, max_num, max_count))
