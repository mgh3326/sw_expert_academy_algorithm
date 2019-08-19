my_dict = {
    'W': 0,
    'B': 1,
    'R': 2
}


def to_russia(blue_index):
    global min_result_value
    temp_result = result_value
    temp_result += my_list[blue_index][0] + my_list[blue_index][2]
    for white_index in range(0, blue_index):
        temp_result += my_list[white_index][1] + my_list[white_index][2]
    for red_index in range(blue_index + 1, len(my_list)):
        temp_result += my_list[red_index][0] + my_list[red_index][1]
    if temp_result < min_result_value:
        min_result_value = temp_result


# TODO 스택 오버플로우가 나온다 왜 그러지
test_case_num = int(input())
for test_case_index in range(test_case_num):
    n, m = map(int, input().split())
    min_result_value = n * m
    result_value = 0
    my_list = []
    for i in range(n):
        temp_str = input()
        temp_list = []
        temp_dict = {
            0: 0,
            1: 0,
            2: 0
        }
        for temp_index in range(len(temp_str)):
            if i == 0:
                if temp_str[temp_index] != 'W':
                    result_value += 1
            elif i == n - 1:
                if temp_str[temp_index] != 'R':
                    result_value += 1
            else:
                temp_dict[my_dict[temp_str[temp_index]]] += 1
        if i != 0 and i != n - 1:
            my_list.append(temp_dict)
    for i in range(len(my_list)):
        to_russia(i)

    print("#" + str(test_case_index + 1), min_result_value)
