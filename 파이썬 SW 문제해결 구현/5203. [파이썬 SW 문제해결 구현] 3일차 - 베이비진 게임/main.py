import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0

    card_list = list(map(int, input().split()))
    current_dir = 1
    a_dict = {}
    b_dict = {}
    current_index = 0
    is_end = False
    for card in card_list:
        if current_dir == 1:
            if card not in a_dict:
                a_dict[card] = 0
            a_dict[card] += 1
            if current_index >= 4:
                a_dict_keys = sorted(list(a_dict.keys()))
                count = 0
                previous_key = -1
                for a_dict_key in a_dict_keys:
                    if previous_key == -1 or a_dict_key - previous_key > 1:
                        count = 1
                    else:
                        count += 1
                    previous_key = a_dict_key
                    if count >= 3 or a_dict[a_dict_key] >= 3:
                        result = 1
                        is_end = True
                        break

        else:
            if card not in b_dict:
                b_dict[card] = 0
            b_dict[card] += 1
            if current_index >= 4:
                b_dict_keys = sorted(list(b_dict.keys()))
                count = 0
                previous_key = -1
                for b_dict_key in b_dict_keys:
                    if previous_key == -1 or b_dict_key - previous_key > 1:
                        count = 1
                    else:
                        count += 1
                    previous_key = b_dict_key
                    if count >= 3 or b_dict[b_dict_key] >= 3:
                        result = 2
                        is_end = True
                        break
        if is_end:
            break
        current_dir *= -1
        current_index += 1

    print("#%d %d" % (test_case_index + 1, result))
