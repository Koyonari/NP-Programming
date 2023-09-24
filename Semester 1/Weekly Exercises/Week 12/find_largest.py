#An Yong Shyan, S10258126B

#Define function
def find_larger(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2
    
#Prompt user for 4 integers
n1 = int(input("Enter the first integer: "))
n2 = int(input("Enter the second integer: "))
n3 = int(input("Enter the third integer: "))
n4 = int(input("Enter the fourth integer: "))

#Call function
n1 = find_larger(n1, n2)
n2 = find_larger(n3, n4)
n1 = find_larger(n1, n2)

#Print result
print("The largest integer is {}".format(n1))