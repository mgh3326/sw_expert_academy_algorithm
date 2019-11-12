import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())

for test_case_index in range(test_case_num):
    is_end = False
    n, m, k = map(int, input().split())
    my_list = list(map(int, input().split()))
    current_index = 0
    for _ in range(k):
        current_index = (current_index + m) % len(my_list)
        if current_index == 0:
            my_list.append(my_list[current_index - 1] + my_list[current_index])
            current_index -= 1
        else:
            my_list.insert(current_index, my_list[current_index - 1] + my_list[current_index])
        # current_index += 1
    print("#%d" % (test_case_index + 1), end="")
    for i in range(10):
        if i == len(my_list):
            break
        print(" %d" % (my_list[-1 - i]), end="")
    print()
