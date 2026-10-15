#  Take two numbers as input. Without using *
# , calculate and print their product
# using += in a way that adds the first number to itself the
# second number of times. (Think carefully.

num1 = int(input("Enter number :- "))
num2 = int(input("Enter number :- "))
product = 0

for i in range(num2):
    product += num1

print(product)