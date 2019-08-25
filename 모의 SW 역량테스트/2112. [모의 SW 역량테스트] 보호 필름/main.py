def dfs(input_value, is_append, n):
    next_value = input_value + 1
    if next_value >= n + 1:
        if is_append == True:
            copy = dfs_temp_list.copy()
            if len(copy) in output_dict:
                output_dict[len(copy)].append(copy)
            else:
                output_dict[len(copy)] = [copy]
        return

    if is_append == False:
        dfs(next_value, False, n)
        dfs(next_value, True, n)

    else:
        dfs_temp_list.append(input_value)

        dfs(next_value, False, n)
        dfs(next_value, True, n)
        dfs_temp_list.remove(input_value)


def is_success():
    current_value = 0
    for _w in range(w):
        count = 0
        for _d in range(d):
            if _d == 0 or film_list[_d][_w] == current_value:
                count += 1
            else:
                count = 1
            current_value = film_list[_d][_w]

            if count >= k:
                break
        if count < k:
            return False
    return True


# TODO 메모리를 남들보다 2배 사용했다. 아마도 부분집합을 이용하는 것을 2번 사용해서 그런듯 하다 부분집합을 효율적으로 구하는 방법을 얼른 공부하도록 해야겠다.
# init
test_case_num = int(input())
for test_case_index in range(test_case_num):
    d, w, k = map(int, input().split())  # M : 총 이동시간, A : BC의 개수
    result = 0
    film_list = []
    home_dict = {}
    is_end = False
    for i in range(d):
        film_list.append(list(map(int, input().split())))
    # D 크기 만큼 부분집합을 만들어낸다. (몇개를 만들어낼지)
    dfs_temp_list = []
    output_dict = {
    }
    dfs(-1, False, d)
    change_dict = output_dict.copy()
    for change_dict_key in change_dict.keys():
        if is_end == True:
            break
        for change_index_list in change_dict[change_dict_key]:
            if is_end == True:
                break
            dfs_temp_list = []
            output_dict = {}
            dfs(-1, False, len(change_index_list))
            a_color_dict = output_dict.copy()

            saved_change_a_list = []
            saved_change_b_list = []

            for a_color_dict_key in a_color_dict.keys():

                for a_color_dict_index_list in a_color_dict[a_color_dict_key]:
                    change_a_list = []
                    change_b_list = []
                    # a_color_dict_index_list 이걸 A 로 변경 나머지는 (change_index_list에 없는건) B로 변경
                    for change_index_list_index in range(len(change_index_list)):
                        if change_index_list_index in a_color_dict_index_list:
                            # A로 변경
                            change_a_list.append(change_index_list[change_index_list_index])
                        else:
                            change_b_list.append(change_index_list[change_index_list_index])

                            # B로 변경
                        # 시도 한다
                    saved_change_a_list.append(change_a_list)
                    saved_change_b_list.append(change_b_list)

            # 가능한지 확인하도록 하자
            for i in range(len(saved_change_a_list)):
                saved_change_a_list_index = saved_change_a_list[i]
                saved_change_b_list_index = saved_change_b_list[i]
                # if saved_change_a_list_index == [2] and saved_change_b_list_index == [5]:
                #     print()
                saved_a = []
                saved_b = []
                for saved_change_a in saved_change_a_list_index:
                    saved_a.append(film_list[saved_change_a].copy())
                    film_list[saved_change_a] = [0] * w
                for saved_change_b in saved_change_b_list_index:
                    saved_b.append(film_list[saved_change_b].copy())
                    film_list[saved_change_b] = [1] * w

                success = is_success()
                if success == True:
                    result = len(change_index_list)
                    is_end = True
                    break
                for idx, saved_change_a in enumerate(saved_change_a_list_index):
                    film_list[saved_change_a] = saved_a[idx]
                for idx, saved_change_b in enumerate(saved_change_b_list_index):
                    film_list[saved_change_b] = saved_b[idx]
    print("#%d %d" % (test_case_index + 1, result))
