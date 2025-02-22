# 1. Square pattern

# n=int(input("Enter the size:"))
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()


# 2.Trailing pattern

n=int(input("Enter size:"))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# for i in range(n):
#     for j in range(n-i):
#         print("*",end="")
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end="")
#     print()


# for i in range(n):
#     for j in range(i+1):
#         print(i+1,end="")
#     print()


# for i in range(n):
#     for j in range(n-i):
#         print(j+1,end="")
#     print()


# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*i+1):
#         print("*",end="")
#     for l in range(n-i):
#         print(" ",end="")
#     print()


for i in range(n):
    for k in range(i+1):
        print("",end="")
    for j in range(2*(n-i)-1):
        print("*",end="")
    for l in range(i+1):
        print("",end="")
    print()