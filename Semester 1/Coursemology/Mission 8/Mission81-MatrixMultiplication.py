#Programming I
#########################
#      Mission 8.1      #
# Matrix Multiplication #
#########################

#Background
#==========
#Tom wants to multiply a 3x3 matrix with a 3x1 matrix.
#Write a Python program to multiply matrix A with matrix B
#and store the result in matrix C, which is a 3x1 matrix.

#Important Notes
#===============
#1) You MUST use the variables, A, B, C

#START CODING FROM HERE
#======================
def matrix_multiplication(A, B):
    C = []
    for i in range(len(A)):
        total = 0
        for j in range(len(B)):
            total += A[i][j] * B[j]
        C.append(total)
    
    return C  # do not remove this line
#Do not remove the next line that calls the function
C = matrix_multiplication(A,B)

#Display the result
print(C)