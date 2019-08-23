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
    remove_list = []
    x_max = -1000
    y_max = -1000
    x_min = 1000
    y_min = 1000
    for i in range(n):
        temp_list = list(map(int, input().split()))
        if temp_list[0] < x_min:
            x_min = temp_list[0]
        if temp_list[0] > x_max:
            x_max = temp_list[0]
        if temp_list[1] < y_min:
            y_min = temp_list[1]
        if temp_list[1] > y_max:
            y_max = temp_list[1]
        temp_list.append(False)
        my_list.append(temp_list)
    while True:
        if len(my_list) == 0:
            break
        for idx, my in enumerate(my_list):
            dir_idx = my[2]
            nx, ny = dx[dir_idx], dy[dir_idx]
            my[0] = my[0] + nx
            my[1] = my[1] + ny
            if my[0] > x_max or my[0] < x_min or my[1] > y_max or my[1] < y_min:  # 튀어 나갔을 경우 1000말고 더 작게 할수도 있을것 같다
                my[4] = True
                heapq.heappush(remove_list, idx * -1)
        for _ in range(len(remove_list)):
            heappop = heapq.heappop(remove_list) * -1
            my_list.pop(heappop)
        for idx, my in enumerate(my_list):
            if my[4] == True:
                continue
            for i in list(range(0, idx)) + list(range(idx + 1, len(my_list))):
                if my_list[i][4] == True:
                    continue
                if (my[0] == my_list[i][0] and my[1] == my_list[i][1]) or (
                        my[0] == my_list[i][0] + 1 and my[1] == my_list[i][1] and my[2] == 2 and my_list[i][
                    2] == 3) or (
                        my[0] == my_list[i][0] - 1 and my[1] == my_list[i][1] and my[2] == 3 and my_list[i][
                    2] == 2) or (
                        my[0] == my_list[i][0] and my[1] == my_list[i][1] + 1 and my[2] == 1 and my_list[i][
                    2] == 0) or (
                        my[0] == my_list[i][0] and my[1] == my_list[i][1] - 1 and my[2] == 0 and my_list[i][2] == 1):
                    result = result + my[3] + my_list[i][3]
                    my[3] = 0
                    my_list[i][3] = 0
                    my[4] = True
                    my_list[i][4] = True
                    heapq.heappush(remove_list, idx * -1)
                    heapq.heappush(remove_list, i * -1)

        for _ in range(len(remove_list)):
            heappop = heapq.heappop(remove_list) * -1
            try:
                my_list.pop(heappop)
            except IndexError:
                continue

    print("#%d %d" % (test_case_index + 1, result))
