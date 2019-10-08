import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())
for test_case_index in range(test_case_num):
    n = int(input())
    number_list = list(map(int, input().split()))
    number_list.sort()
    start_index = 0
    end_index = len(number_list) - 1
    result_list = []
    for i in range(5):
        if start_index > end_index:
            break
        result_list.append(number_list[end_index])
        if end_index == start_index:
            break
        result_list.append(number_list[start_index])
        end_index -= 1
        start_index += 1

    result = str.join(" ", map(str, result_list))
    print("#%d %s" % (test_case_index + 1, result))
