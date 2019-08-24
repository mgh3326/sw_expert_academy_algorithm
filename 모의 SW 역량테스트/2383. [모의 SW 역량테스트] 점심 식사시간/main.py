import copy

dx = [1, 0, -1, 0]  # Right, down, left, up
dy = [0, 1, 0, -1]


def dfs(input_value, is_append):  # 부분집합
    next_value = input_value + 1
    if (next_value > len(person_list)):
        if is_append == True:
            saved_a_list.append(copy.deepcopy(a_list))
        return
    if is_append == True:
        a_list.append(input_value)
        dfs(next_value, True)
        dfs(next_value, False)
        a_list.remove(input_value)
    else:
        dfs(next_value, True)
        dfs(next_value, False)


# init
test_case_num = int(input())
for test_case_index in range(test_case_num):
    n = int(input())
    result = -1
    room_list = []
    person_list = []
    stair_list = []

    for i in range(n):
        temp_list = list(map(int, input().split()))  # M : 총 이동시간, A : BC의 개수
        for j in range(len(temp_list)):
            if temp_list[j] == 1:  # 사람일 경우
                person_list.append((i, j))
            elif temp_list[j] > 1:  # 계단 일 경우
                stair_list.append([(i, j), temp_list[j]])
        room_list.append(temp_list)
    a_list = []
    saved_a_list = []
    # TODO 부분 집합 만들기에서 시간을 많이 사용하였다. 최적화가 요구된다.
    dfs(-1, False)  # 부분 집합을 만든다.
    # 부분 집합의 중간의 있는 값을 이용해서 찍기 확률을 높혀준다. (바이너리 서치를 이용해도 좋을것 같다.)
    # pop = saved_a_list.pop(len(saved_a_list) // 2)
    # saved_a_list.insert(0, pop)
    # 별로 안 빠르다
    for saved_a in saved_a_list:
        # if saved_a == [0, 1, 2, 3]:
        #     print()
        stair_a_list = []
        stair_b_list = []
        for idx, person in enumerate(person_list):
            if idx in saved_a:  # 1번 계단 조건
                distance = abs(person[0] - stair_list[0][0][0]) + abs(person[1] - stair_list[0][0][1])
                stair_a_list.append(distance)
            else:  # 2번 계단 조건
                distance = abs(person[0] - stair_list[1][0][0]) + abs(person[1] - stair_list[1][0][1])
                stair_b_list.append(distance)

        current_a_list = []
        current_b_list = []
        count = 0
        remove_list = []
        last_count = 0

        while True:
            if len(stair_a_list) == 0 and len(stair_b_list) == 0 and len(current_a_list) == 0 and len(
                    current_b_list) == 0 and last_count == 0:
                if result == -1 or result > count:
                    result = count
                break
            count += 1
            if result != -1 and count > result:
                break
            last_count = 0
            for idx in reversed(range(len(stair_a_list))):
                stair_a_list[idx] -= 1
                if stair_a_list[idx] == -1:
                    current_a_list.append(stair_list[0][1])
                    stair_a_list.pop(idx)
            for idx in reversed(range(len(stair_b_list))):
                stair_b_list[idx] -= 1
                if stair_b_list[idx] == -1:
                    current_b_list.append(stair_list[1][1])
                    stair_b_list.pop(idx)
            for idx in reversed(range(len(current_a_list[:3]))):
                current_a_list[idx] -= 1
                if current_a_list[idx] == 0:
                    current_a_list.pop(idx)
                    last_count = 1
            for idx in reversed(range(len(current_b_list[:3]))):
                current_b_list[idx] -= 1
                if current_b_list[idx] == 0:
                    current_b_list.pop(idx)
                    last_count = 1

    print("#%d %d" % (test_case_index + 1, result))
