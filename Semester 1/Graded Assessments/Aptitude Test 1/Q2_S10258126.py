#An Yong Shyan (S10258126) - IT03

import re

#Prompt user for ID
id = input('Enter an ID: ')

#Differentiate if ID is student or staff
if re.search('[-]', id) is not None:
    list(id)
    l = id[3:]
    id = id.lower()
    u = id[:2]
    email = (l + '@' + u + '.abc.edu.sg')
    
else:
    id = id.lower()
    email = id + '@abc.edu.sg'

#Print out email
print('Email Address:', email)
