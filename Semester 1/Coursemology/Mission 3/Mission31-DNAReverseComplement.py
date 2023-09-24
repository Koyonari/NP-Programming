#Programming I

#####################################
#      Mission 3.1                  #
#     DNA Reverse Complement        #
#####################################

#Background
#==========
#String Manipulation techniques are often applied in the field of DNA sequence analysis.
#In a double-stranded DNA, if the sequence of one of the strands is given from top to bottom,
#the sequence of other strand from bottom to top (reverse complement) can be found.
#
#The corresponding complement of each base that can occur in a DNA strand is as follows:
#A=T, C=G, G=C, T=A
#
#Therefore, if given a 7-base long DNA sequence 'ACCGTCG', the corresponding complement
#sequence is 'TGGCAGC'. The reverse would be 'CGACGGT', which gives the sequence of the other
#DNA strand.

#Write a program that prompts for input of the sequence (7 base long) of a DNA strand in a
#double-stranded DNA, and displays the sequence of the other DNA strand.


#Important Notes
#===============
#1) You are required to include a function called calculate_DNAReverseComplement(), which
#   accepts a string of DNA sequence, find and returns its reverse complement
#2) When testing the program in IDLE, you should prompt the user for the input value.
#   However, you must comment out the input prompt before submitting it in coursemology


#START CODING FROM HERE
#======================

#The possible bases in a DNA sequence and their complements
base = 'ACGT'
complement = 'TGCA'
#Hint: There is no need to edit/remove the previous 2 lines.


#Do not edit/remove the next line
def calculate_DNAReverseComplement(dna1):
    dna1 = dna1.lower()
    base1 = base.lower()

    for i in range(4):
        dna1 = dna1.replace(base1[i], complement[i])
    
    #Code to obtain dna2, the reverse complement of dna1
    dna2 = dna1[::-1]

    return dna2 #Do not edit/remove this line


#Prompt for input of one DNA sequence and store in dna1. You must remove this
#statement when submitting in Coursemology
dna1 = str(input('Enter a 7-base long DNA sequence: '))

#Do not edit/remove the next line that calls the function 
dna2 = calculate_DNAReverseComplement(dna1)

#Modify the statement to display the dna2
print(dna2)


#input 'ACCGTCG' #output 'CGACGGT'
#input 'TGCATGC' #output 'GCATGCA'