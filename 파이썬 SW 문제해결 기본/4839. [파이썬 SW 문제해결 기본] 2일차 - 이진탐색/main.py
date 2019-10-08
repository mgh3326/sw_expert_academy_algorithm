import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())


def binary_search(left, right, value):
    count = 0
    while True:
        center = (left + right) // 2
        count += 1
        if center == value:
            break
        elif center < value:
            left = center
        elif center > value:
            right = center
    return count


for test_case_index in range(test_case_num):
    result = "0"
    current_sum = 0
    P, A, B = (map(int, input().split()))
    a_count = binary_search(1, P, A)
    b_count = binary_search(1, P, B)
    if a_count > b_count:
        result = "B"
    elif a_count < b_count:
        result = "A"
    print("#%d %s" % (test_case_index + 1, result))
