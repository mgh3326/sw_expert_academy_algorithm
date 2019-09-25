test_case_num = 10
for test_case_index in range(test_case_num):
    input()
    left, right = map(int, input().split())
    current_count = pow(left, right)
    print("#%d %d" % (test_case_index + 1, current_count))
