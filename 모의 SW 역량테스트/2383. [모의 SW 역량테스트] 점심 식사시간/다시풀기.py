import sys

sys.stdin = open("data/sample_input.txt")


def dfs(depth, start_idx):
    global result

    if depth == size:
        current_tuple = tuple(current_set)
        if current_tuple in save_set:  # 백트래킹
            return
        difference = total_set.difference(current_tuple)
        difference_tuple = tuple(difference)
        save_set.add(current_tuple)
        save_set.add(difference_tuple)
        for first_tuple, second_tuple in [(current_tuple, difference_tuple), (difference_tuple, current_tuple)]:
            current_time = 0
            second_stair_person_list = []
            for value in second_tuple:
                second_stair_person_list.append(memo_list[1][value])
            first_stair_person_list = []
            for value in first_tuple:
                first_stair_person_list.append(memo_list[0][value])
            first_stair_person_list.sort()
            second_stair_person_list.sort()
            a_idx = 0
            b_idx = 0
            a_list = []
            b_list = []
            while True:
                if len(a_list) == 0 and len(b_list) == 0 and a_idx >= len(first_stair_person_list) and b_idx >= len(
                        second_stair_person_list):
                    break
                while True:
                    if a_idx < len(first_stair_person_list) and first_stair_person_list[a_idx] <= current_time:
                        if len(a_list) < 3:
                            a_list.append(board_list[stair_list[0][0]][stair_list[0][1]])
                            a_idx += 1
                        else:
                            break
                    else:
                        break
                while True:
                    if b_idx < len(second_stair_person_list) and second_stair_person_list[b_idx] <= current_time:
                        if len(b_list) < 3:
                            b_list.append(board_list[stair_list[1][0]][stair_list[1][1]])
                            b_idx += 1
                        else:
                            break
                    else:
                        break
                save_idx = 0
                for idx in range(len(a_list)):
                    a_list[idx] -= 1
                    if a_list[idx] == 0:
                        save_idx = idx + 1
                a_list = a_list[save_idx:]
                save_idx = 0
                for idx in range(len(b_list)):
                    b_list[idx] -= 1
                    if b_list[idx] == 0:
                        save_idx = idx + 1
                b_list = b_list[save_idx:]
                current_time += 1
            if result == -1 or result > current_time:
                result = current_time
        return
    for i in range(start_idx, len(person_list)):
        current_set.add(i)
        dfs(depth + 1, i + 1)
        current_set.remove(i)


T = int(input())
for test_case_idx in range(T):
    result = -1
    N = int(input())
    board_list = [list(map(int, input().split())) for _ in range(N)]
    save_set = set()
    person_list = []
    stair_list = []
    for h in range(N):
        for w in range(N):
            if board_list[h][w] == 1:
                person_list.append((h, w))
            elif board_list[h][w] > 1:
                stair_list.append((h, w))
    total_set = set(i for i in range(len(person_list)))
    memo_list = [[0 for _ in range(len(person_list))] for _ in range(len(stair_list))]
    for h in range(len(stair_list)):
        for w in range(len(person_list)):
            memo_list[h][w] = abs(person_list[w][0] - stair_list[h][0]) + abs(person_list[w][1] - stair_list[h][1]) + 1

    for size in range(len(person_list) // 2 + 1):  # 조건이 애매하게 들어갔었다
        current_set = set()
        dfs(0, 0)
    print("#%d %d" % (test_case_idx + 1, result))
