# An Yong Shyan, 10258126B

import re

# Prompt user to input password
pw = str(input('Enter password: '))

# Check if password is valid
if len(pw) >= 8:
    if re.search('\d', pw) is not None:
        if re.search('[A-Z]', pw) is None:
            print('Password must contain at least one uppercase letter.')
        elif re.search('[a-z]', pw) is None:
            print('Password must contain at least one lowercase letter.')
        else:
            print('Password is valid.')
    else:
        print('Password must contain at least one digit.')
else:
    print('Password must be at least 8 characters long.')