import sys

sys.stdin = open("./input.txt")

test_case_num = int(input())

for test_case_index in range(test_case_num):
    result = "error"
    stack = []
    board_list = input().split()
    for board in board_list:
        if board.isdigit():
            stack.append(int(board))
        else:
            if board == "+" or board == "-" or board == "*" or board == "/":
                if len(stack) < 2:
                    break
                second = stack.pop()
                first = stack.pop()
                temp = 0
                if board == "+":
                    temp = first + second
                if board == "-":
                    temp = first - second
                if board == "*":
                    temp = first * second
                if board == "/":
                    if second == 0:
                        break
                    temp = first // second
                stack.append(temp)
            elif board == ".":
                if len(stack) != 1:
                    break
                else:
                    result = stack.pop()
                    break
    print("#%d %s" % (test_case_index + 1, result))
