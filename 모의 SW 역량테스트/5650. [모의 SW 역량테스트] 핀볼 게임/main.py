dx = [1, 0, -1, 0]  # Right, down, left, up
dy = [0, 1, 0, -1]


def pinball_game(input_h, input_w, dir_idx):
    count = 0
    is_start = True
    while True:
        if is_start == False and input_h == start_point[0] and input_w == start_point[1]:
            return count
        is_start = False
        # if start_point == (1, 3) and _dir_idx == 0:
        #     print()
        nx, ny = dx[dir_idx], dy[dir_idx]
        next_h = input_h + ny
        next_w = input_w + nx
        if next_h < 0 or next_h >= n or next_w < 0 or next_w >= n:  # 범위 초과 벽 튕김 되버린다
            dir_idx = (dir_idx + 2) % 4  # 이럼 오른쪽은 왼쪽 이런게 되버린다. (거꾸로 가능 개꿀 따리따리)
            count += 1
            next_h, next_w = input_h, input_w
        next_value = my_list[next_h][next_w]
        if next_value == 0:  # 얼른 다음 번호로 뛰어가야되
            input_h = next_h
            input_w = next_w
            continue
        if next_value == -1:  # 블랙홀 발견
            return count
        if next_value >= 6:  # 웜홀일 경우
            warm_hall_index = block_dict[next_value].index((next_h, next_w))
            input_h, input_w = block_dict[next_value][(warm_hall_index + 1) % 2]
            continue
        else:  # 블록을 만나버린경우
            if next_value == 1:
                if dir_idx == 0 or dir_idx == 3:  # 튕겨 버립니다.
                    dir_idx = (dir_idx + 2) % 4  # 이럼 오른쪽은 왼쪽 이런게 되버린다. (거꾸로 가능 개꿀 따리따리)
                elif dir_idx == 1:
                    dir_idx = 0
                elif dir_idx == 2:
                    dir_idx = 3
            elif next_value == 2:
                if dir_idx == 0 or dir_idx == 1:  # 튕겨 버립니다.
                    dir_idx = (dir_idx + 2) % 4  # 이럼 오른쪽은 왼쪽 이런게 되버린다. (거꾸로 가능 개꿀 따리따리)
                elif dir_idx == 2:
                    dir_idx = 1
                elif dir_idx == 3:
                    dir_idx = 0
            elif next_value == 3:
                if dir_idx == 1 or dir_idx == 2:  # 튕겨 버립니다.
                    dir_idx = (dir_idx + 2) % 4  # 이럼 오른쪽은 왼쪽 이런게 되버린다. (거꾸로 가능 개꿀 따리따리)
                elif dir_idx == 0:
                    dir_idx = 1
                elif dir_idx == 3:
                    dir_idx = 2
            elif next_value == 4:
                if dir_idx == 2 or dir_idx == 3:  # 튕겨 버립니다.
                    dir_idx = (dir_idx + 2) % 4  # 이럼 오른쪽은 왼쪽 이런게 되버린다. (거꾸로 가능 개꿀 따리따리)
                elif dir_idx == 0:
                    dir_idx = 3
                elif dir_idx == 1:
                    dir_idx = 2
            elif next_value == 5:
                dir_idx = (dir_idx + 2) % 4  # 이럼 오른쪽은 왼쪽 이런게 되버린다. (거꾸로 가능 개꿀 따리따리)
            input_h, input_w = next_h, next_w
            count += 1


# init
test_case_num = int(input())
for test_case_index in range(test_case_num):
    n = int(input())
    # 입력의 첫 번째 줄은 배열의 행 수입니다.
    current_count = 0
    max_result = 0
    warm_hall_list = []
    block_dict = {}
    my_list = []  # 맵 정보
    for i in range(n):
        temp_list = list(map(int, input().split()))
        for w in range(len(temp_list)):
            # bolck dict에 저장하는건데 이렇게 0인걸 따로 저장하는게 더 효율적인지는 더 생각해볼 필요가 있을것 같다.
            if temp_list[w] <= 0 or temp_list[w] >= 6:
                if temp_list[w] in block_dict:
                    block_dict[temp_list[w]].append((i, w))
                else:
                    block_dict[temp_list[w]] = [(i, w)]
                    if temp_list[w] >= 6:
                        warm_hall_list.append(temp_list[w])

        my_list.append(temp_list)
    for start_point in block_dict[0]:  # 시작점과 방향을 조건으로 주고 result를 비교하도록 하면 아주 깔끔히 풀릴것 같다.
        for _dir_idx in range(4):
            result_count = pinball_game(input_h=start_point[0], input_w=start_point[1], dir_idx=_dir_idx)
            # print(start_point, _dir_idx, result_count)
            if max_result < result_count:
                max_result = result_count
    print("#%d %d" % (test_case_index + 1, max_result))
