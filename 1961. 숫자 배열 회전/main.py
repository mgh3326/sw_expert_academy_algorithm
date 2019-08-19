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
    n = int(input())
    result_value = 0
    my_list = []
    result1_list = []
    result2_list = []
    result3_list = []
    for i in range(n):
        temp_list = list(map(int, input().split()))
        my_list.append(temp_list)
        result1_list.append([0] * n)
        result2_list.append([0] * n)
        result3_list.append([0] * n)
    for h in range(n):
        for w in range(n):
            result1_list[w][n - h - 1] = my_list[h][w]
            result2_list[n - h - 1][n - w - 1] = my_list[h][w]
            result3_list[n - w - 1][h] = my_list[h][w]

    print("#" + str(test_case_index + 1))
    for i in range(n):
        for j in range(n):
            print(result1_list[i][j], end="")
        print(" ", end="")

        for j in range(n):
            print(result2_list[i][j], end="")
        print(" ", end="")
        for j in range(n):
            print(result3_list[i][j], end="")
        print()
