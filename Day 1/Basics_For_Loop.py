"""------Basic for loops-----
    Print numbers 1 to N
    Print even/odd numbers 1 to N
    Print table of a number
    Sum of 1 to N using a loop"""

# 1) Print numbers 1 to N

n=10
for element in range(1, n+1):
    print (element)

#Print even/odd numbers 1 to N
n=10
for element in range(1, n+1):
    if element%2==0:
        print(f"{element} is even")
    else:
        print(f"{element} is odd")

#Print table of a number
num = int(input("Enter a number: "))
limit = int(input("Number of Iteration: "))
print(f"Multiplication Table of {num}:\n")
for i in range(1, limit + 1):
    print(f"{num} x {i} = {num * i}")

#Sum of 1 to N using a loop

n=10
for i in range(n):
    n+=i
    
print(n)







