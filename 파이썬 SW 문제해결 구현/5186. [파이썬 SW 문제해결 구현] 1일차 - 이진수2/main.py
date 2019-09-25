test_num = int(input())
for test_index in range(test_num):
    num = float(input())
    current_count = ""
    index = 1
    while True:
        if num >= pow(2, -1 * index):
            num = num - pow(2, -1 * index)
            current_count += "1"
            if num == 0:
                break
        else:
            current_count += "0"
        index += 1
        if len(current_count) == 12:
            current_count = "overflow"
            break

    print("#%d %s" % (test_index + 1, current_count))
