import sys

sys.stdin = open("./data/input.txt")

dh = [0, 0, -1, 1]  # 왼,오,위,아
dw = [-1, 1, 0, 0]  # 왼,오,위,아
test_case_num = int(input())
for test_case_index in range(test_case_num):
    result = "NO"
    r, c = map(int, input().split())
    my_list = []
    visit_dict = {}
    goal_count = 0
    for i in range(r):
        temp_str = input()
        goal_count += temp_str.count("@")
        my_list.append(temp_str)
    if goal_count == 0:
        print("#%d %s" % (test_case_index + 1, result))
        continue
    current_h, current_w = 0, 0
    current_dir = 1
    save_memory = 0
    queue = [[current_h, current_w, current_dir, save_memory]]
    while True:
        if len(queue) == 0:
            break
        if result == "YES":
            break
        current_h, current_w, current_dir, save_memory = queue.pop(0)
        while True:
            current_value = my_list[current_h][current_w]
            if (current_h, current_w) not in visit_dict:
                visit_dict[(current_h, current_w)] = set()
            if (save_memory, current_dir) in visit_dict[(current_h, current_w)]:  # 무한루프
                break
            visit_dict[(current_h, current_w)].add((save_memory, current_dir))
            if current_value.isnumeric():
                save_memory = int(current_value)
            elif current_value == "<":
                current_dir = 0
            elif current_value == ">":
                current_dir = 1
            elif current_value == "^":
                current_dir = 2
            elif current_value == "v":
                current_dir = 3
            elif current_value == "_":
                if save_memory == 0:
                    current_dir = 1
                else:
                    current_dir = 0
            elif current_value == "|":
                if save_memory == 0:
                    current_dir = 3
                else:
                    current_dir = 2
            elif current_value == "?":
                for dir_idx in range(len(dh)):
                    next_h = (current_h + dh[dir_idx]) % r
                    next_w = (current_w + dw[dir_idx]) % c
                    queue.append([next_h, next_w, dir_idx, save_memory])
                break
            elif current_value == ".":
                pass
            elif current_value == "+":
                save_memory = (save_memory + 1) % 16
            elif current_value == "-":
                save_memory = (save_memory - 1) % 16
            elif current_value == "@":
                result = "YES"
                break

            current_h = (current_h + dh[current_dir]) % r
            current_w = (current_w + dw[current_dir]) % c
    print("#%d %s" % (test_case_index + 1, result))
