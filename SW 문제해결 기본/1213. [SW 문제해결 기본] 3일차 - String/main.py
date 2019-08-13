test_case_num = 10
for i in range(10):
    test_index_input = int(input())
    find_string = input()
    total_string = input()
    result_count = total_string.count(find_string)
    print("#%d %d" % (test_index_input, result_count))
