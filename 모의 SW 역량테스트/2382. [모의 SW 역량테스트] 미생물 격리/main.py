dh = [-1, 1, 0, 0]  # 상 하 좌 우
dw = [0, 0, -1, 1]


def change_dir(input_dir):
    if input_dir == 0:
        return 1
    if input_dir == 1:
        return 0
    if input_dir == 2:
        return 3
    if input_dir == 3:
        return 2


# init
test_case_num = int(input())
for test_case_index in range(test_case_num):
    n, m, k = map(int, input().split())  # M : 총 이동시간, A : BC의 개수
    result = 0
    runway_list = []
    microorganism_dict = {}
    # microorganism_list = []
    # for i in range(n):
    #     if i == 0 or i == n - 1:
    #         temp_list = [1] * n
    #
    #     else:
    #         temp_list = [1] + [0] * (n - 2) + [1]
    #
    #     microorganism_list.append(temp_list)

    for _ in range(k):
        temp_list = list(map(int, input().split()))  # M : 총 이동시간, A : BC의 개수
        microorganism_dict[(temp_list[0], temp_list[1])] = [temp_list[2], temp_list[3] - 1]
        result += temp_list[2]
    for m_index in range(m):
        next_microorganism_dict = {}
        overlap_dict = {}
        for microorganism_point in microorganism_dict.keys():
            microorganism_size, microorganism_dir = microorganism_dict[microorganism_point]
            nh, nw = dh[microorganism_dir], dw[microorganism_dir]
            new_point = microorganism_point[0] + nh, microorganism_point[1] + nw
            if new_point[0] == 0 or new_point[1] == 0 or new_point[0] == n - 1 or new_point[1] == n - 1:  # 모서리에 닿을 경우
                if microorganism_size // 2 != 0:

                    next_microorganism_dict[new_point] = [microorganism_size // 2, change_dir(microorganism_dir)]
                    result = result - (microorganism_size - (microorganism_size // 2))
                else:
                    result -= microorganism_size
            else:
                if new_point in next_microorganism_dict:  # 중복이 있는 경우
                    if new_point in overlap_dict:
                        overlap_dict[new_point].append([microorganism_size, microorganism_dir])
                    else:
                        overlap_dict[new_point] = [next_microorganism_dict[new_point]]
                        overlap_dict[new_point].append([microorganism_size, microorganism_dir])

                else:
                    next_microorganism_dict[new_point] = [microorganism_size, microorganism_dir]
        for overlap_dict_key in overlap_dict.keys():
            temp_sum = overlap_dict[overlap_dict_key][0][0]
            temp_max = overlap_dict[overlap_dict_key][0][0]
            temp_dir = overlap_dict[overlap_dict_key][0][1]
            for overlap in overlap_dict[overlap_dict_key][1:]:
                temp_sum += overlap[0]
                if temp_max < overlap[0]:
                    temp_max = overlap[0]
                    temp_dir = overlap[1]
            next_microorganism_dict[overlap_dict_key] = [temp_sum, temp_dir]
        microorganism_dict = next_microorganism_dict
    print("#%d %d" % (test_case_index + 1, result))
