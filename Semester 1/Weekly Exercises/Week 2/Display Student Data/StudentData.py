#Read the file
with open('StudentData.txt', 'r') as f:
    contents = f.read()
    contents = contents.splitlines()
        #Loop to check line number
    for i, line in enumerate(contents):
            if i==0 or i==2 or i ==4:
                print(line.strip())
