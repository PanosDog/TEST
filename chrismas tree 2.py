N = int(input('give a number of high tree: '))
for i in range(0,N):
    for j in range(0,N-i-1):
        print(" ", end="")
    for j in range(0,2*i+1):
        print("*", end="")
    print("")
