#Programming I

#######################
#     Mission 9.1     #
#   MartrixMultiply   #
#######################

#Background
#==========
#Tom has studied about creating 3D games and wanted
#to write a function to multiply 2 matrices.
#Define a function MaxtrixMulti() function with 2 parameters.
#Both parameters are in a matrix format.


#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[2,0,0],
     [0,2,0],
     [0,0,2]]

#START CODING FROM HERE
#======================
#Create your function here
def matrixmult(A, B):
     # Check if len(row of A) == len(column of B)
     assert len(A[0]) == len(B)

     # Flip B across it's axis
     B = list(zip(*B))

     # Calculate each product and put into answer
     answer = []
     for i in range(len(A)):
          result = []
          for j in range(len(B)):
               result.append(sum([a * b for a, b in zip(A[i], B[j])]))
          answer.append(result)

     return answer
   
#Do not remove the next line
answer = matrixmult(A, B)

#3) For testing, print out the output
#   - Comment out before submitting
print(answer)