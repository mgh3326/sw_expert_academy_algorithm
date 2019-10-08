import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    password_dict = {
        "0001101": 0,
        "0011001": 1,
        "0010011": 2,
        "0111101": 3,
        "0100011": 4,
        "0110001": 5,
        "0101111": 6,
        "0111011": 7,
        "0110111": 8,
        "0001011": 9,
    }
    n, m = map(int, input().split())
    board_list = []
    oh_text = ""
    for i in range(n):
        temp_txt = input()
        if len(board_list) > 0:
            continue
        find = temp_txt.find("1")
        if find != -1:
            oh_text = temp_txt
            last_index = temp_txt.rindex("1")
            while True:
                index_ = temp_txt[last_index - 6:last_index + 1]
                if index_ == "0" * 7 or len(index_) < 7:
                    break
                board_list.append(password_dict[index_])
                last_index -= 7
    board_list.reverse()
    odd_sum = 0
    even_sum = 0
    for i in range(len(board_list)):
        value = board_list[i]
        if i % 2 == 0:
            odd_sum += value
        else:
            even_sum += value
    temp_result = odd_sum * 3 + even_sum
    if temp_result % 10 != 0:
        result = 0
    else:
        result = odd_sum + even_sum
    print("#%d %d" % (test_case_index + 1, result))
