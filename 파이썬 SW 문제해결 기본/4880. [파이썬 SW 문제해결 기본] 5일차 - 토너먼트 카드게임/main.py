import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())


def rock_paper_scissors(left, right):
    left_value = left[0]
    right_value = right[0]
    if left_value == right_value:
        return left
    elif left_value == 1:
        if right_value == 2:
            return right
        elif right_value == 3:
            return left
    elif left_value == 2:
        if right_value == 1:
            return left
        elif right_value == 3:
            return right
    elif left_value == 3:
        if right_value == 1:
            return right
        elif right_value == 2:
            return left


# TODO merge sort를 단순히 list를 복사하는 방식으로 하였는데 index로 짜는것이 더욱 효율적일 것이라고 생각된다.
def find_winner(current_list):
    if len(current_list) == 2:
        left, right = current_list
        return rock_paper_scissors(left, right)
    if len(current_list) == 1:
        return current_list[0]
    mid = (0 + len(current_list) - 1) // 2
    left_list = current_list[:mid + 1]
    right_list = current_list[mid + 1:]
    left = find_winner(left_list)
    right = find_winner(right_list)
    return rock_paper_scissors(left, right)


for test_case_index in range(test_case_num):
    n = int(input())
    board_list = list(map(int, input().split()))
    for i in range(len(board_list)):
        board_list[i] = (board_list[i], i + 1)
    result_value, result = find_winner(board_list)
    print("#%d %s" % (test_case_index + 1, result))
