import sys

sys.stdin = open("./data/sample_input.txt")
# TODO result값을 마지막에 계산하기보다 매번 갱신 해주는게 더 속도를 높힐수 있겠다.
# (상: 1, 하: 2, 좌: 3, 우: 4) -> 1씩 빼주는걸로 하자
dir_list = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]
T = int(input())
for test_case_idx in range(T):
    N, M, K = map(int, input().split())
    virus_dict = {}
    for virus_idx in range(K):
        r, c, n, k = map(int, input().split())
        virus_dict[virus_idx + 1] = [r, c, n, k - 1]
    count = 0
    result = 0
    while True:
        if count == M:
            for virus_dict_key in virus_dict.keys():
                result += virus_dict[virus_dict_key][2]
            break
        board_list = [[0 for _ in range(N)] for _ in range(N)]
        temp_dict = {}
        remove_list = []
        for virus_dict_key in virus_dict.keys():
            r, c, n, k = virus_dict[virus_dict_key]
            dh, dw = dir_list[k]
            nh, nw = r + dh, dw + c
            if nh == 0 or nw == 0 or nh == N - 1 or nw == N - 1:
                if k % 2 == 0:
                    k += 1
                else:
                    k -= 1
                next_value = n // 2
                if next_value > 0:
                    virus_dict[virus_dict_key] = [nh, nw, next_value, k]
                    board_list[nh][nw] = virus_dict_key
                else:
                    # virus_dict.pop(virus_dict_key)  # 이렇게 지워지면 영향을 받나 -> 받네
                    remove_list.append(virus_dict_key)
            else:
                virus_dict[virus_dict_key][0] = nh
                virus_dict[virus_dict_key][1] = nw
                if board_list[nh][nw] != 0:
                    if (nh, nw) not in temp_dict:
                        temp_dict[nh, nw] = []
                        temp_dict[nh, nw].append(board_list[nh][nw])
                    temp_dict[nh, nw].append(virus_dict_key)
                else:
                    board_list[nh][nw] = virus_dict_key
        for remove in remove_list:
            virus_dict.pop(remove)
        for temp_dict_key in temp_dict.keys():
            max_value = 0
            max_dir = 0
            max_idx = 0
            current_sum = 0
            for idx in temp_dict[temp_dict_key]:
                r, c, n, k = virus_dict[idx]
                if n > max_value:
                    max_value = n
                    max_dir = k
                    max_idx = idx
                current_sum += n
            for idx in temp_dict[temp_dict_key]:
                if max_idx == idx:
                    virus_dict[idx][2] = current_sum
                else:
                    virus_dict.pop(idx)
        count += 1
    print("#%d %d" % (test_case_idx + 1, result))
