import heapq
import copy

dx = [1, 0, -1, 0]  # Right, down, left, up
dy = [0, 1, 0, -1]
person_dx = [0, 1, 0, -1]  # 상, 우, 하, 좌
person_dy = [-1, 0, 1, 0]


def dfs(input_point):
    for dir_idx in range(4):
        nx, ny = dx[dir_idx], dy[dir_idx]
        new_x = input_point[0] + nx
        new_y = input_point[1] + ny
        if new_x <= 0 or new_y <= 0 or new_x > width_map or new_y > height_map:
            continue
        distance = (abs(new_x - bc_point[0])) + (abs(
            new_y - bc_point[1]))
        if distance <= scale:
            new_point = (new_x, new_y)
            if new_point not in bc_dict:
                bc_dict[new_point] = [power_index]
                dfs(new_point)
            else:
                if power_index not in bc_dict[new_point]:
                    bc_dict[new_point].append(power_index)
                    dfs(new_point)


# init
test_case_num = int(input())
for test_case_index in range(test_case_num):
    m, a = map(int, input().split())  # M : 총 이동시간, A : BC의 개수
    user_num = 2
    width_map = 10
    height_map = 10
    user_list = []
    bc_list = []
    bc_dict = {}
    result = 0
    power_list = []
    for _ in range(user_num):
        user_list.append(list(map(int, input().split())))
    for _a_index in range(a):
        temp_list = (list(map(int, input().split())))
        heapq.heappush(bc_list, (temp_list[3] * -1, ((temp_list[0], temp_list[1]), temp_list[2], _a_index)))
        power_list.append(temp_list[3])
    for _ in range(len(bc_list)):
        power, (bc_point, scale, power_index) = heapq.heappop(bc_list)
        power *= -1
        if bc_point not in bc_dict:
            bc_dict[bc_point] = [power_index]
        else:
            bc_dict[bc_point].append(power_index)
        dfs(bc_point)
    a_start_point = [1, 1]
    b_start_point = [10, 10]
    for m_idx in range(m + 1):
        a_list = []
        b_list = []
        a_list_top = None
        b_list_top = None
        if tuple(a_start_point) in bc_dict:
            a_list = copy.deepcopy(bc_dict[tuple(a_start_point)])
        if tuple(b_start_point) in bc_dict:
            b_list = copy.deepcopy(bc_dict[tuple(b_start_point)])

        # TODO 가능한 조건중에 최대값을 구할수 있어야한다.
        if len(a_list) > 0:
            a_list_top = a_list.pop(0)
        if len(b_list) > 0:
            b_list_top = b_list.pop(0)
        if a_list_top != None or b_list_top != None:
            if a_list_top == None:
                result += power_list[b_list_top]
            elif b_list_top == None:
                result += power_list[a_list_top]
            elif a_list_top != None and b_list_top != None:
                if a_list_top == b_list_top:
                    if len(a_list) == 0 and len(b_list) == 0:
                        result += power_list[b_list_top]
                    elif len(a_list) == 0:
                        result += power_list[a_list_top]
                        pop = b_list.pop(0)
                        result += power_list[pop]
                    elif len(b_list) == 0:
                        result += power_list[b_list_top]
                        pop = a_list.pop(0)
                        result += power_list[pop]
                    else:
                        a_pop_value = power_list[a_list.pop(0)]
                        b_pop_value = power_list[b_list.pop(0)]
                        result += max(a_pop_value, b_pop_value)
                        result += power_list[a_list_top]

                else:
                    result += power_list[b_list_top]
                    result += power_list[a_list_top]
        if m_idx == m:
            break

        a_dir_dix = user_list[0][m_idx] - 1
        b_dir_dix = user_list[1][m_idx] - 1
        if a_dir_dix != -1:
            a_start_point[0] += person_dx[a_dir_dix]
            a_start_point[1] += person_dy[a_dir_dix]
        if b_dir_dix != -1:
            b_start_point[0] += person_dx[b_dir_dix]
            b_start_point[1] += person_dy[b_dir_dix]

    print("#%d %d" % (test_case_index + 1, result))
