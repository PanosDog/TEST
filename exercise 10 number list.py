N = 31
my_list= []
my_list_1 = []
my_list_2 = []
for i in range(N):
    if i >=10 and i % 2 == 0 and i<=20:
        my_list.append(i)
    elif i >= 10 and i <=20:
        my_list_1.append(i)
    elif i > 1 and i % 3 == 0 and i < 30:
        my_list_2.append(i)
    i += 1
print(my_list)
my_list_1.sort()
my_list_1.reverse()
print(my_list_1)
print(my_list_2)

