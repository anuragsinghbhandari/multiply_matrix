import numpy as np

#creating  a function to create a n order matrix
def create_matrix(matrix_name, size):
  matrix_name = np.ones((size,size), dtype=np.int64)
  for i in range(0, size):
    for j in range(0, size):
      matrix_name[i,j]=int(input("Enter a"+str(i+1)+str(j+1)+": "))
  return matrix_name

#creating matrix using above function
A = create_matrix("A", 3)

#function to multiply matrices
def matrix_multiply(matrix_A ):
  mul_result=np.ones(matrix_A.shape,dtype='int64')
  for i in range(0,len(matrix_A[0])):
    for j in range(0,len(matrix_A[0])):
      sum=0
      for k in range(0,len(matrix_A[0])):
        #three number per loop to add
        sum+=matrix_A[i,k]*matrix_A[k,j]
      #adding sum to matrix
      mul_result[i,j]=sum
  return(mul_result)
print(matrix_multiply(A))

  

