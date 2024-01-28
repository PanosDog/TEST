my_list = []
N = int(input("give a number between 3 and 20: "))
while N < 3 or N > 20:
    N = int(input("give a number again between 3 and 20: "))

for i in range(N):
    number = int(input("give a number between 10 and 20: "))
    while number > 20 or number < 10:
        number = int(input("give again a number between 10 and 20: "))
    my_list.append(number)


my_list.sort()
print(my_list)
print(len(my_list))
