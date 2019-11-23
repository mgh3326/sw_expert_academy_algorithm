import sys

sys.stdin = open("./data/input.txt")

import heapq

test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = 0
    N, M, K, _A, _B = map(int, input().split())
    A = _A - 1
    B = _B - 1
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    visit_list = [[0 for _ in range(M)] for _ in range(N)]
    coming_list = list(map(int, input().split()))
    current_a_list = [[0, 0] for i in range(N)]  # 남은 시간, 고객 번호
    waiting_a_list = []
    waiting_b_list = []
    current_b_list = [[0, 0, 0] for i in range(M)]  # 남은 시간, 고객 번호, 이전 창구 번호
    empty_a_list = [i for i in range(N)]
    empty_b_list = [i for i in range(M)]
    heapq.heapify(empty_a_list)
    heapq.heapify(empty_b_list)
    coming_idx = 0
    current_time = 0
    while True:
        if coming_idx >= len(coming_list) and len(waiting_a_list) == 0 and len(waiting_b_list) == 0 and len(empty_a_list)==N:
            break
        # A waiting 에 담기
        while True:
            if coming_idx < len(coming_list):
                if coming_list[coming_idx] <= current_time:
                    waiting_a_list.append(coming_idx + 1)
                    coming_idx += 1
                else:
                    break  # sort가 되었다면
            else:
                break
        # A counter에 가자
        while True:
            if len(waiting_a_list) > 0 and len(empty_a_list) > 0:
                idx = heapq.heappop(empty_a_list)
                current_a_list[idx] = [a_list[idx], waiting_a_list.pop(0)]
            else:
                break
        if len(empty_a_list) != N:
            for i in range(N):
                if i in empty_a_list:
                    continue
                current_a_list[i][0] -= 1
                if current_a_list[i][0] == 0:
                    heapq.heappush(empty_a_list, i)
                    waiting_b_list.append([current_a_list[i][1], i])
        # B counter에 가자
        while True:
            if len(waiting_b_list) > 0 and len(empty_b_list) > 0:
                idx = heapq.heappop(empty_b_list)
                customer_id, a_idx = waiting_b_list.pop(0)
                current_b_list[idx] = [b_list[idx], customer_id, a_idx]
                if a_idx == A and idx == B:
                    result += customer_id
            else:
                break

        if len(empty_b_list) != M:
            for i in range(M):
                if i in empty_b_list:
                    continue
                current_b_list[i][0] -= 1
                if current_b_list[i][0] == 0:
                    heapq.heappush(empty_b_list, i)
                    # waiting_b_list.append([current_b_list[1], i])
        current_time += 1
    if result == 0:
        result = -1
    print("#%d %d" % (test_case_index + 1, result))
