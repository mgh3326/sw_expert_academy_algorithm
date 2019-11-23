import sys

sys.stdin = open("./data/sample_input.txt")

import heapq

dir_list = [
    [0, 0],
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
]
test_case_num = int(input())

for test_case_idx in range(test_case_num):
    result = 0
    charge_dict = {}
    charge_list = []
    M, A = map(int, input().split())
    a_dir_list = list(map(int, input().split()))
    b_dir_list = list(map(int, input().split()))
    for i in range(A):
        x, y, c, p = map(int, input().split())
        charge_list.append(p)
        h = y - 1
        w = x - 1
        visit_set = set()
        visit_set.add((h, w))
        queue = []  # TODO 충전량 크기가 같을수 있을수도 있겠다
        queue.append((h, w, 0))
        queue_idx = 0
        while True:
            if queue_idx >= len(queue):
                break
            h, w, cost = queue[queue_idx]
            if (h, w) not in charge_dict:
                charge_dict[h, w] = []
            heapq.heappush(charge_dict[h, w], (p * -1, i))
            for dh, dw in dir_list[1:]:
                nh = dh + h
                nw = dw + w
                if nh < 0 or nw < 0 or nh >= 10 or nw >= 10 or (nh, nw) in visit_set:
                    continue
                if cost < c:
                    visit_set.add((nh, nw))
                    queue.append((nh, nw, cost + 1))
            queue_idx += 1
    a_h = 0
    a_w = 0
    b_h = 9
    b_w = 9
    idx = 0
    while True:

        if (a_h, a_w) in charge_dict and (b_h, b_w) in charge_dict:  # 둘다 있을 때
            temp_max = 0
            for (first_h, first_w), (second_h, second_w) in [((a_h, a_w), (b_h, b_w)),
                                                             ((b_h, b_w), (a_h, a_w))]:  # 0 : A먼저 1 : B 먼저
                temp_value = 0
                heappop = heapq.heappop(charge_dict[first_h, first_w])
                temp_value += heappop[0] * -1
                first_idx = heappop[1]
                heapq.heappush(charge_dict[(first_h, first_w)], heappop)

                heappop = heapq.heappop(charge_dict[second_h, second_w])
                second_idx = heappop[1]
                if second_idx == first_idx:
                    if len(charge_dict[second_h, second_w]) > 0:
                        heappop2 = heapq.heappop(charge_dict[second_h, second_w])
                        temp_value += heappop2[0] * -1
                        heapq.heappush(charge_dict[(second_h, second_w)], heappop2)
                else:
                    temp_value += heappop[0] * -1
                heapq.heappush(charge_dict[(second_h, second_w)], heappop)
                temp_max = max(temp_max, temp_value)
            result += temp_max

        else:
            for h, w in [(a_h, a_w), (b_h, b_w)]:  # 하나만 있거나 둘다 없을 때
                if (h, w) in charge_dict:
                    heappop = heapq.heappop(charge_dict[(h, w)])
                    result += heappop[0] * -1
                    heapq.heappush(charge_dict[(h, w)], heappop)
        if idx == M:
            break
        a_h += dir_list[a_dir_list[idx]][0]
        a_w += dir_list[a_dir_list[idx]][1]
        b_h += dir_list[b_dir_list[idx]][0]
        b_w += dir_list[b_dir_list[idx]][1]
        idx += 1
    print("#%d %d" % (test_case_idx + 1, result))
