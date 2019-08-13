test_num = int(input())
for test_index in range(test_num):
    input_temp = (input().split())
    hex_length = int(input_temp[0])
    hex_list = input_temp[1]
    result = ""
    for _hex in hex_list:
        num = (int(_hex, 16))
        for i in reversed(range(4)):
            if num >= pow(2, i):
                num = num - pow(2, i)
                result += "1"
            else:
                result += "0"

    print("#%d %s" % (test_index + 1, result))
