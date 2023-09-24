#Programming I
#######################
#     Mission 7.1     #
#     Process File    #
#######################

#Background
#Tom has created a text file. He would like to know the number of
#lines, words and characters in the file. He indicates that spaces 
#and end-of-line characters are also considered characters.
#Help him read the data file and perform the counting and return
#the number of lines, words and characters as a list.
#
#E.g. if your data file contains the 2 lines below
#Hello World
#I like Python Programming
#The return value should be [ 2,6,38 ]
#Important Notes

#===============
#1) Comment out ALL input prompts before submitting.
#2) The data file to be used is 'datafile.txt'
#START CODING FROM HERE

#======================
#function to process the file
def process_file(filename):
    infile = open(filename) # open the file
    datafile = infile.read() # read the file
    #code to process the file and count number of lines, words and characters
    lines = datafile.strip().splitlines()
    lineCount = len(lines)
    words = datafile.strip().replace('\n', ' ').split(' ')
    wordCount = len(words)
    charCount = len(datafile)
    infile.close() # close file
    return [lineCount, wordCount, charCount] #return the values

# Prompt user for the file name - remove it before submitting in Coursemology
# filename = input("Enter filename: ")
# Call function - remove it before submitting in Coursemology
result = process_file("datafile.txt")

# Modify to print the output as shown in the question
print("Total number of lines:", result[0])
print("Total number of words:", result[1])
print("Total number of characters:", result[2])
print(result)