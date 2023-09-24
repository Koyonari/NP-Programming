#AN Yong Shyan, S10258126B

#Define function
def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result

#Prompt user for input
x = int(input("Enter the base: "))
n = int(input("Enter the exponent: "))

#Call function
result = power(x, n)

#Print result
print("{} to the power of {} is {}".format(x, n, result))