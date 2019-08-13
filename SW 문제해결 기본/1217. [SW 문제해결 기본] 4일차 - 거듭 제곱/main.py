test_case_num = 10
for test_case_index in range(test_case_num):
    input()
    left, right = map(int, input().split())
    result = pow(left, right)
    print("#%d %d" % (test_case_index + 1, result))
