temp_list = [0, 1, 2, 3]
for i in range(10):
    print(i, (i + 2) % 4)
    # 이럼 오른쪽은 왼쪽 이런게 되버린다. (거꾸로 가능 개꿀 따리따리)
    print(i, (i + 2) % 4, temp_list[(i + 2) % 4])
