import sys

sys.stdin = open("./input.txt")


def is_palindrome(input_str):
    if len(input_str) < 2:
        return False
    for i in range(len(input_str) // 2):
        if input_str[i] != input_str[len(input_str) - 1 - i]:
            return False
    return True


def generate_substr(input_str):
    global result
    global is_end
    for i in range(len(input_str) - m + 1):
        substr = input_str[i:i + m]
        if is_palindrome(substr):
            result = substr
            is_end = True
            return


test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = ""
    is_end = False
    n, m = map(int, input().split())
    board_list = []
    for _ in range(n):
        temp_str = input()
        board_list.append(temp_str)
    # substring
    for board in board_list:
        generate_substr(board)
        if is_end:
            break
    if not is_end:
        for w in range(n):
            temp_str = ""
            for h in range(n):
                temp_str += board_list[h][w]
            generate_substr(temp_str)
            if is_end:
                break
    # 회문인지 비교하는 함수
    print("#%d %s" % (test_case_index + 1, result))
