my_list = []
for  i in range(10):
    x = int(input("give a number between 10 and 20: "))
    if x > 20 or x < 10 :
       x = input("give a correct number between 10 and 20: ")
    my_list.append(x)
my_tuple = tuple(my_list)
print(my_tuple)
list_square = []
for i in range(10) :
    list_square.append(my_list[i]**2)
print(list_square)

list_square.sort()
print(list_square)