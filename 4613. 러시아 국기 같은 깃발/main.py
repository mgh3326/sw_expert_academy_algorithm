dx = [1, 0, -1, 0]  # Right, down, left, up
dy = [0, 1, 0, -1]

test_case_num = int(input())
for test_case_index in range(test_case_num):
    n, m = map(int, input().split())
    result_value = []
    max_value = 0
    current_value = 0
    my_list = []
    check_list = []
    for i in range(n):
        temp: str = input()
        my_list.append(temp)
    for i in range(n):
        for j in range(n):
            check_list[i][j] = True
            start_value = my_list[i][j]
            dfs(i, j)
            check_list[i][j] = False

    print("#" + str(test_case_index + 1), result_value, max_value + 1)
