def operating_cost(input_k):
    return (input_k * input_k) + (input_k - 1) * (input_k - 1)


# init
test_case_num = int(input())
for test_case_index in range(test_case_num):
    n, m = map(int, input().split())  # M : 총 이동시간, A : BC의 개수
    result = 0
    home_list = []
    home_dict = {}
    microorganism_dict = {}

    for i in range(n):
        temp_list = list(map(int, input().split()))  # M : 총 이동시간, A : BC의 개수
        for j in range(n):
            if temp_list[j] == 1:
                home_dict[(i, j)] = 0
        home_list.append(temp_list)
    all_sum = len(home_dict) * m

    for i in range(n):
        for j in range(n):
            start_point = (i, j)
            operating_distance = 0
            while True:
                count = 0
                for home_dict_key in home_dict.keys():
                    distance = abs(home_dict_key[0] - start_point[0]) + abs(home_dict_key[1] - start_point[1])
                    if distance <= operating_distance:
                        count += 1
                if count * m >= operating_cost(operating_distance + 1):  # 가능 ^^
                    if result < count:
                        result = count
                operating_distance += 1
                if operating_cost(operating_distance + 1) >= all_sum:
                    break
    print("#%d %d" % (test_case_index + 1, result))
