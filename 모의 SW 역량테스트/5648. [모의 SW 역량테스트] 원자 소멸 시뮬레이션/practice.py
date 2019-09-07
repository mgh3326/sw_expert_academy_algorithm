my_list = [1, 2, 3, 4]
idx = 1
for i in list(range(0, idx))+list(range(idx + 1, len(my_list))) :
    print(i)
# for i in range(idx + 1, len(my_list)):
#     print(i)
