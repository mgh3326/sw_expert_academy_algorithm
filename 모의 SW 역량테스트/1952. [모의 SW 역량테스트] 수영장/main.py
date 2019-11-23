import sys

sys.stdin = open("data/sample_input.txt")


# 8시 14분

def generate_queter(depth, start_idx):
    if depth == 3:
        for temp in temp_list:
            if value_list[temp] != 0:
                first_list.append(temp_list.copy())
                break
        return
    for idx in range(start_idx, 12):
        if depth != 0 and idx - temp_list[-1] > 1:
            return
        temp_list.append(idx)
        generate_queter(depth + 1, idx + 1)
        temp_list.pop()


def dfs(depth, start_idx):
    global result
    if depth == size:
        temp_current_list = []
        for current in current_list:
            temp_current_list.extend(first_list[current])
        current_value = size * quater
        for i in range(12):
            if i not in temp_current_list:
                current_value += value_list[i]
        if result == -1 or result > current_value:
            result = current_value
        return
    for idx in range(start_idx, len(first_list)):
        if depth != 0:
            is_continue = False
            for current in current_list:
                if len(set(set(first_list[current])).intersection(set(first_list[idx]))) > 0:
                    is_continue = True
                    break
            if is_continue:
                continue
        current_list.append(idx)
        dfs(depth + 1, idx + 1)
        current_list.pop()


T = int(input())
for test_case_idx in range(T):
    result = -1
    day, month, quater, year = map(int, input().split())
    my_list = list(map(int, input().split()))
    value_list = []
    for my in my_list:
        value_list.append(min(day * my, month))
    # 한달을 보면서, Day로 하는게 나을지, Month로 하는게 나을지 정한다
    # 이후에 발생한 Month를 3달치로 묶어본다 이중에서 최소값을 찾는다 (1,2,3) (4,5,6) (7,8,9)
    temp_list = []
    first_list = []
    if value_list[11] != 0:
        first_list.append([11])
    if value_list[11] != 0 or value_list[10] != 0:
        first_list.append([10, 11])
    generate_queter(0, 0)
    for size in range(5):
        current_list = []
        dfs(0, 0)
    result = min(result, year)
    print("#%d %d" % (test_case_idx + 1, result))
