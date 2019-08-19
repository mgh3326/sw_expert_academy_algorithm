my_list = [0, 1, 2, 3]


def my_func(value):
    for _i in range(0, value):
        print(_i)
    print("===============================")
    for _i in range(value + 1, len(my_list)):
        print(_i)


for i in range(len(my_list)):
    print("============", i)
    my_func(i)
