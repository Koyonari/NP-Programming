#An Yong Shyan, S10258126B

# Define function
def find_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# Number list
num_list = [10, -13, 50, 5, 7, 24, 65, -40, 44, 30]

# Print results
print('Even numbers:')
even_numbers = [n for n in num_list if find_even(n)]
print(even_numbers)