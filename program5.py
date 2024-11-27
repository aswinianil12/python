num = int(input("Enter a number :"))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print(f"factorial of a number is {fact}")
limit = int(input("Enter the limit:\n"))
print("fibonacci series are:")
num1 = 0
num2 = 1
print(num1)
print(num2)
for i in range(3,limit+1):
    nextnum=num1 + num2
    print(nextnum)
    num1 = num2
    num2 = nextnum

num_list=[1,2,3,4,5]
print(f"The list is:{num_list}")
total=sum(num_list)
print(f"sum of all items in the list:{total}")

