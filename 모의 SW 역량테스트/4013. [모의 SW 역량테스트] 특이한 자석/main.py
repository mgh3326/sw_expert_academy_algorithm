test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    k = int(input())
    n = 4
    # 입력의 첫 번째 줄은 배열의 행 수입니다.
    magnet_list = []  # 자석 정보
    rotate_list = []  # 자석 회전 정보

    for i in range(n):
        magnet_list.append(list(map(int, input().split())))
    for i in range(k):
        rotate_list.append(list(map(int, input().split())))
    for rotate in rotate_list:
        rotate_direction = rotate[1]
        rotate_index = rotate[0] - 1
        temp_rotate_direction = rotate[1] * -1
        temp_rotate_list = []
        for _rotate_index in reversed(range(0, rotate_index)):
            if magnet_list[_rotate_index][2] != magnet_list[_rotate_index + 1][6]:
                temp_rotate_list.append([_rotate_index + 1, temp_rotate_direction])
                temp_rotate_direction *= -1
            else:
                break
        temp_rotate_direction = rotate[1] * -1

        for _rotate_index in range(rotate_index + 1, 4):
            if magnet_list[_rotate_index - 1][2] != magnet_list[_rotate_index][6]:
                temp_rotate_list.append([_rotate_index + 1, temp_rotate_direction])
                temp_rotate_direction *= -1
            else:
                break
        if rotate_direction == 1:  # 오른쪽으로 회전
            pop = magnet_list[rotate_index].pop()
            magnet_list[rotate_index].insert(0, pop)

        else:  # 왼쪽으로 회전
            rotate__pop = magnet_list[rotate_index].pop(0)
            magnet_list[rotate_index].append(rotate__pop)
        for temp_rotate in temp_rotate_list:
            rotate_direction = temp_rotate[1]
            rotate_index = temp_rotate[0] - 1
            if rotate_direction == 1:  # 오른쪽으로 회전
                pop = magnet_list[rotate_index].pop()
                magnet_list[rotate_index].insert(0, pop)

            else:  # 왼쪽으로 회전
                rotate__pop = magnet_list[rotate_index].pop(0)
                magnet_list[rotate_index].append(rotate__pop)
    for idx, magnet in enumerate(magnet_list):
        result += 2 ** idx * magnet[0]

    print("#%d %d" % (test_case_index + 1, result))
