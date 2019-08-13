test_num = 10
horizontal_scale = 100
for test_index in range(test_num):
    dump_num = int(input())
    box_list = list(map(int, input().split()))

    for dump_index in range(dump_num):
        max_box_list = max(box_list)
        min_box_list = min(box_list)

        if max_box_list - min_box_list <= 1:
            break
        max_box_list_index = box_list.index(max(box_list))
        min_box_list_index = box_list.index(min(box_list))

        box_list[min_box_list_index] = box_list[min_box_list_index] + 1
        box_list[max_box_list_index] = box_list[max_box_list_index] - 1
    print("#%d %d" % (test_index + 1, max(box_list) - min(box_list)))

# a, b = map(int, input().split())
