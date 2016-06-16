# Matrix Algebra

import numpy as np
import math

# Addition/Substraction 
def add_sub(a,b,f):
 if a.shape != b.shape:
  return "Matrices should be of the same order"
 else:
  row = a.shape[0]
  col = a.shape[1]
  result = np.zeros((row,col))
  for i in range(row):
   for j in range(col):
    if f == 'a':
     result[i,j] = a[i,j] + b[i,j]
    else:
     result[i,j] = a[i,j] - b[i,j]
  return result
# Product of matrices
def prod(u,v):
 if u.shape[1]!=v.shape[0]:
  return "Number of columns of first matrix should be equal to number of rows of second matrix"
 else:
  return np.dot(u,v)
  
# Magnitude of vectors
def mag(u):
 sqsum =0
 for i in range(u.shape[0]):
  for j in range(u.shape[1]):
   sqsum = sqsum + (u[i,j]*u[i,j])
  return math.sqrt(sqsum)
  
#Dot product of vectors  
def dotprod(u,v):
 result = np.zeros((u.shape[0],u.shape[1]))
 for i in range(u.shape[0]):
  for j in range(u.shape[1]):
   result[i,j] = (u[i,j]*v[i,j])
 return result

#Product of a matrix and a scalar 
def scalar_prod(mat,alpha):
 result = mat * alpha
 return result
 
# Exercise
a= np.matrix([[1,2,3],[2,7,4]])
b = np.matrix([[1,-1],[0,1]])
c = np.matrix([[5,-1],[9,1],[6,0]])
d = np.matrix([[3,-2,-1],[1,2,3]])
u = np.matrix([[6,2,-3,5]])
v = np.matrix([[3,5,-1,4]])
w = np.matrix([[1],[8],[0],[5]])
alpha = 6

# Dimensions 
print("Dimensions of the matrices:")
print("A:",a.shape,"\nB:",b.shape,"\nC:",c.shape,"\nD:",d.shape,"\nu:",u.shape,"\nv:",v.shape,"\nw:",w.shape)
# Vector Operations
print("Vector Operations:")
print("u+v :",add_sub(u,v,'a'),"\nu-v :",add_sub(u,v,'s'),"\nalpha*u :",scalar_prod(u,alpha),"\nDot product of u,v :",dotprod(u,v),"\nMagnitude of u:",mag(u))
# Matrix Operations
print("Matrix Operations:")
print("A+C :",add_sub(a,c,'a'),
"\n A-CT:",add_sub(a,c.T,'s'),
"\nCT+3D :",add_sub(c.T,scalar_prod(d,3),'a'),
"\nBA:",prod(b,a),
"\nBAT:",prod(b,a.T))
#optional
print("BC:",prod(b,c),"\n CB:",prod(c,b),"\n B4:",prod(b,prod(b,prod(b,b))),"\nAAT:",prod(a,a.T),"\nDTD:",prod(d.T,d))

'''
Results:
Dimensions of the matrices:
A: (2, 3)
B: (2, 2)
C: (3, 2)
D: (2, 3)
u: (1, 4)
v: (1, 4)
w: (4, 1)
Vector Operations:
u+v : [[ 9.  7. -4.  9.]]
u-v : [[ 3. -3. -2.  1.]]
alpha*u : [[ 36  12 -18  30]]
Dot product of u,v : [[ 18.  10.   3.  20.]] 
Magnitude of u: 8.602325267042627
Matrix Operations:
A+C : Matrices should be of the same order
 A-CT: [[-4. -7. -3.]
 [ 3.  6.  4.]]
CT+3D : [[ 14.   3.   3.]
 [  2.   7.   9.]]
BA: [[-1 -5 -1]
 [ 2  7  4]]
BAT: Number of columns of first matrix should be equal to number of rows of second matrix
BC: Number of columns of first matrix should be equal to number of rows of second matrix
 CB: [[ 5 -6]
 [ 9 -8]
 [ 6 -6]]
 B4: [[ 1 -4]
 [ 0  1]]
AAT: [[14 28]
 [28 69]]
DTD: [[10 -4  0]
 [-4  8  8]
 [ 0  8 10]]

'''
