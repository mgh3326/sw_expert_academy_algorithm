arr_size = 100
test_case_num = 10
for test_case_index in range(test_case_num):
    temp_list = []
    visited_list = []
    stack = list()
    for i in range(100):
        temp_list.append(list())
        visited_list.append(False)

    _, order_pair_num = map(int, input().split())
    order_pair_list = list(map(int, input().split()))

    for order_pair_index in range(order_pair_num):
        temp_list[order_pair_list[order_pair_index * 2]].append(order_pair_list[order_pair_index * 2 + 1])
        print(order_pair_list[order_pair_index * 2], order_pair_list[order_pair_index * 2 + 1])
    current_index=0
    while True:
        visited_list[current_index]=True
        stack.append(current_index)

        stack.pop()
        current_index


    print("end")
