test_num = int(input())
for test_index in range(test_num):
    num = float(input())
    result = ""
    index = 1
    while True:
        if num >= pow(2, -1 * index):
            num = num - pow(2, -1 * index)
            result += "1"
            if num == 0:
                break
        else:
            result += "0"
        index += 1
        if len(result) == 12:
            result = "overflow"
            break

    print("#%d %s" % (test_index + 1, result))
