def left_check(point):
    w, h = point
    for _width in range(w):
        if map_list[h][_width] != 0:
            for __width in range(_width):
                map_list[h][__width] = 0

            map_list[h][w] = 3
            return
        else:
            map_list[h][_width] = 1
    for _width in range(w):
        map_list[h][w] = 2


test_case_num = int(input())
for test_case_index in range(test_case_num):
    n = int(input())
    # 입력의 첫 번째 줄은 배열의 행 수입니다.
    map_list = []
    # 입력을 받되 첫줄 혹은 끝줄의 경우 2(전선 연결 완료)로 표시하도록 하자
    saved_list = []
    for i in range(n):
        temp_list = list(map(int, input().split()))
        if i == 0 or i == n - 1:
            for temp in temp_list:
                if temp == 1:
                    temp_list[temp_list.index(temp)] = 2
        else:
            for temp in temp_list:
                if temp_list.index(temp) == 0 or temp_list.index(temp) == n - 1:
                    if temp == 1:
                        temp_list[temp_list.index(temp)] = 2
                        saved_list.append((i, temp_list.index(temp)))
                else:
                    if temp == 1:
                        saved_list.append([(i, temp_list.index(temp)), False])

        map_list.append(temp_list)
    left_check(saved_list[0][0])
    saved_list[0][1] = True

    print()
    max_num = max(map_list)
    max_num_index_list = [i for i, val in enumerate(map_list) if val == max_num]
    # 와 코드를 이렇게도 짤수 있구나 if 저게 True면 i를 반환하나보다 멋지다리
