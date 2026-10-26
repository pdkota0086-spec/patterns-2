print("half pramid stars pattern (*)")
n = int(input("enter the number of rows :"))
for i in range(n):
    for j in range (i+1):
        print("*",end="  " )
    print()

print("half pramid stars pattern (numbers), floyd's triangle")
n = int(input("enter the number of rows :"))
number = 1
for i in range(n):
    for j in range (i+1):
        print(number,end="  ")
        number = number + 1
    print()


n = int(input("enter the number of rows :"))

for i in range(1,n+1):
    print(" " * (n-i) + "*" * i)

print("half pramid stars pattern (*)")
n = int(input("enter the number of rows :"))
for i in range(n):
    for j in range (i+1):
        print("*", number ,end="  ")
        number = number + 1
    print()