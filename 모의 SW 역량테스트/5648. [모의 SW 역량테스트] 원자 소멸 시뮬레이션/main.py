import heapq

dx = [0, 0, -1, 1]  # up, down, left, right (원자 전용임) 다른 곳에서는 사용하지 말아야한다!
dy = [1, -1, 0, 0]

# init
test_case_num = int(input())
for test_case_index in range(test_case_num):
    n = int(input())
    # 입력의 첫 번째 줄은 배열의 행 수입니다.
    result = 0
    warm_hall_list = []
    block_dict = {}
    my_list = []  # 맵 정보
    first_remove_list = []
    x_max = -2000
    y_max = -2000
    x_min = 2000
    y_min = 2000

    for i in range(n):
        temp_list = list(map(int, input().split()))
        temp_list[0] *= 2
        temp_list[1] *= 2
        if temp_list[0] < x_min:
            x_min = temp_list[0]
        if temp_list[0] > x_max:
            x_max = temp_list[0]
        if temp_list[1] < y_min:
            y_min = temp_list[1]
        if temp_list[1] > y_max:
            y_max = temp_list[1]
        my_list.append(temp_list)

    while True:
        atom_map_dict = {
        }
        remove_list = []
        remove_atom_list = []
        if len(my_list) <= 1:
            break
        for my_list_idx in range(len(my_list)):
            my = my_list[my_list_idx]
            dir_idx = my[2]
            nx, ny = dx[dir_idx], dy[dir_idx]
            my[0] = my[0] + nx
            my[1] = my[1] + ny
            if my[0] > x_max or my[0] < x_min or my[1] > y_max or my[1] < y_min:  # 튀어 나갔을 경우 1000말고 더 작게 할수도 있을것 같다
                remove_list.append(my_list_idx)
            else:
                if (my[0], my[1]) in atom_map_dict:
                    if atom_map_dict[(my[0], my[1])] == 1:
                        remove_atom_list.append((my[0], my[1]))
                else:
                    atom_map_dict[(my[0], my[1])] = 1

        for my_list_idx in reversed(range(len(my_list))):
            my = my_list[my_list_idx]
            if len(remove_list) > 0:
                if my_list_idx == remove_list[-1]:
                    my_list.pop(my_list_idx)
                    remove_list.pop()
                    continue
            if (my[0], my[1]) in remove_atom_list:
                result += my[3]
                my_list.pop(my_list_idx)
    print("#%d %d" % (test_case_index + 1, result))
