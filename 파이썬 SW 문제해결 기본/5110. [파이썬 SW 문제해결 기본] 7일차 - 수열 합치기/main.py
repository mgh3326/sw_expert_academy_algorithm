import sys

sys.stdin = open("./input.txt")


def merge(input_list):
    global my_list
    for i in range(len(my_list)):
        if my_list[i] > input_list[0]:
            input_list.extend(my_list[i:])

            my_list = my_list[:i]
            my_list.extend(input_list)
            break
    else:
        my_list.extend(input_list)


test_case_num = int(input())
for test_case_index in range(test_case_num):
    is_end = False
    result = 0
    n, m = map(int, input().split())
    my_list = []
    for _ in range(m):
        temp_list = list(map(int, input().split()))
        merge(temp_list)
    result_list = []
    print("#%d" % (test_case_index + 1), end="")
    for idx in range(10):
        print(" %d" % (my_list[-1 - idx]), end="")
    print()
