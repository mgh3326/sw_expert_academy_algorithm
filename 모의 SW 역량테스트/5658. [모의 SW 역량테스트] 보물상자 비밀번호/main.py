test_case_num = int(input())

for test_case_index in range(test_case_num):
    n, k = map(int, input().split())
    current_count = 0
    s = input()
    my_list = []
    count = 0
    split_size = n // 4
    my_dict = {}

    while True:

        if count == n:
            break
        my_list.append(s[count: count + split_size])
        count += split_size
    for i in range(split_size):
        for my in my_list:
            if my not in my_dict:
                my_dict[my] = True
        temp_list = []
        for my_list_index in range(len(my_list)):
            temp_list.append(my_list[my_list_index - 1][-1] + my_list[my_list_index][:split_size - 1])
        my_list = temp_list
    l = sorted(my_dict.keys(), reverse=True)
    # for _l in l:

    k_ = int(l[k-1], 16)

    print("#" + str(test_case_index + 1), k_)
