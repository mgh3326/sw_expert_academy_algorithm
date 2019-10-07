import sys

sys.stdin = open("./input.txt")
# TODO 문제 이해가 안간다
test_case_num = int(input())


def binary_search(input_list, find_value, left, right):
    is_left = False
    left_count = 0
    is_right = False
    right_count = 0
    is_found = False
    while True:
        if left > right:
            break
        mid = (left + right) // 2
        if find_value < input_list[mid]:
            right = mid - 1
            is_left = True
            left_count += 1
        elif find_value > input_list[mid]:
            left = mid + 1
            is_right = True
            right_count += 1
        elif find_value == input_list[mid]:
            is_found = True

            break
    if is_found:
        if is_left and is_right:
            return True
        elif left_count == 0 or right_count == 0:
            return True
        else:
            return False

    else:
        return False


for test_case_index in range(test_case_num):
    n, m = map(int, input().split())

    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))
    result = 0
    for m in m_list:
        if binary_search(n_list, m, 0, len(n_list) - 1):
            result += 1
    print("#%d %d" % (test_case_index + 1, result))
