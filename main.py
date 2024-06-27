print("Enter an interval")
a = int(input("Start: "))
b = int(input("End: "))

for j in range(a,b):
    for i in range(2,j):
        c = j % i
        if j == 2:
            print(j,"is a prime number!!")
            break
        if c == 0:
            break
   