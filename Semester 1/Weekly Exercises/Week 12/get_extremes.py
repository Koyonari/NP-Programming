#An Yong Shyan, S10258126B

#Define function
def get_extremes():
    num_list.sort()
    return num_list[0], num_list[-1]

#List of integers
num_list = [10, -13, 50, 5, 7, 65, -40, 44, 30 ]

#Print results
print(get_extremes())