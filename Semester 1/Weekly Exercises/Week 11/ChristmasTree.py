#An Yong Shyan, S10258126B

char = input("Enter a character: ")
num = int(input("Enter a number: "))

for row in range(num):
    space = ' ' * (num - (row + 1))
    print(space, end = '')
    star = '* ' * (row + 1)
    print(star)

print('Merry Christmas!')