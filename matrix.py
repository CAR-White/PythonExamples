# Rounding factor in calculations
r = 4

# Get the values for a 2x2 matrix
print('Input the values a,b,c,d for the matrix:')
print('[a b]')
print('[c d]')

# The user inputs the values
print('Input a: ',end='')
a = float(input())
print('Input b: ',end='')
b = float(input())
print('Input c: ',end='')
c = float(input())
print('Input d: ',end='')
d = float(input())

# Construct the matrix from the values
M1 = [[ a, b,], 
      [ c, d,]]

#To print the matrix
#print(M1)

#print(M1[0])
#print('')

#print(M1[0][0])
#print(M1[0][1])
#print(M1[1][0])
#print(M1[1][1])
#print('')

# Compute the determinant
Det = M1[0][0]*M1[1][1] - M1[0][1]*M1[1][0]

# Compute the inverse determinant
InvDet = 1/Det

#InvM1 = [[ InvDet*d, -InvDet*b,], 
#        [ -InvDet*c,InvDet*a,]]

# Compute the inverse matrix components using the InvDet
Inv_a = InvDet*d
Inv_b = -1*InvDet*b
Inv_c = -1*InvDet*c
Inv_d = InvDet*a

# Compute the inverse of the matrix
InvM1 = [[ round(Inv_a,r), round(Inv_b,r),], 
         [ round(Inv_c,r), round(Inv_d,r),]]

# Compute the product of matrix and its inverse

Prod_a = a*Inv_a + b*Inv_c
Prod_b = a*Inv_b + b*Inv_d
Prod_c = c*Inv_a + d*Inv_c
Prod_d = c*Inv_b + d*Inv_d

Prod_M1_InvM1 = [[ round(Prod_a,r), round(Prod_b,r),], 
                 [ round(Prod_c,r), round(Prod_d,r),]]


# Output the results
print('The determinant of the matrix:')
print('')

print(M1[0])
print(M1[1])
print('')

print('is', round(Det,r))
print('... and the inverse is:')
print('')

print(InvM1[0])
print(InvM1[1])
print('')
print('Check by multiplying your matrix by its inverse. We should get the identity, I:')
print('')
print(Prod_M1_InvM1[0])
print(Prod_M1_InvM1[1])


