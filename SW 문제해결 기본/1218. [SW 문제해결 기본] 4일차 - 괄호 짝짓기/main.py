my_dict = {"}": "{",
           ")": "(",
           "]": "[",
           ">": "<",
           }
test_case_num = 10
for test_case_index in range(10):
    str_length = int(input())
    input_str = input()
    str_list = list(input_str)
    temp_list = []
    result = 1
    for _str in str_list:
        if _str == "{" or _str == "(" or _str == "[" or _str == "<":
            temp_list.append(_str)
        else:
            if len(temp_list) == 0:
                result = 0
                break
            if my_dict[_str] != temp_list.pop():
                result = 0
    if len(temp_list) != 0:
        result = 0

    print("#%d %d" % (test_case_index + 1, result))
