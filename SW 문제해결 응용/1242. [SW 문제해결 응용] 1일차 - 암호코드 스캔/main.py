import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    password_dict = {
        "0001101": 0,
        "00000011110011": 0,
        "0011001": 1,
        "00001111000011": 1,
        "0010011": 2,
        "00001100001111": 2,
        "0111101": 3,
        "00111111110011": 3,
        "0100011": 4,
        "00110000001111": 4,
        "0110001": 5,
        "00111100000011": 5,
        "0101111": 6,
        "00110011111111": 6,
        "0111011": 7,
        "00111111001111": 7,
        "0110111": 8,
        "00111100111111": 8,
        "0001011": 9,
        "00000011001111": 9,
    }
    n, m = map(int, input().split())
    board_list = []
    for i in range(n):
        temp_txt = input()
        if len(board_list) > 0:
            continue
        find = temp_txt.find("1")
        if find != -1:
            my_text = "0" * 14 + bin(int(temp_txt, 16))[2:]
            last_index = my_text.rindex("1")
            while True:
                index_ = my_text[last_index - 6:last_index + 1]
                if index_.__eq__("0000000") or (len(index_) < 7):
                    break
                if index_ not in password_dict:
                    index_ = my_text[last_index - 6 - 7:last_index + 1]
                    last_index -= 7
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
