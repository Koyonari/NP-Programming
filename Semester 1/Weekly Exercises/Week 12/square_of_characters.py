#An Yong Shyan, S10258126B

# Define function
def print_square(side):
    for i in range(side):
        print(char * side)

# Prompt user for input
side = int(input("Enter the side length: "))
char = input("Enter the character: ")

# Call function
print_square(side)