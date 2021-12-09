import numpy as np

# create array using numpy
arr = np.array([0,1,2,3,4,5])
# print(arr.size)


# Vector addition and subtraction

##
# python code
# #
u = [1,0]
v = [1,0]
z= []
for n, m in zip(u,v):
    z.append(n+m)
    
#print(z)


###
# numpy code (it's runc much faster then requalr python code)
# #
u_nb = np.array([1,0])
v_nb = np.array([0,1])
z_add_nb = u_nb + v_nb
#print(z_add_nb)

z_sub_nb = u_nb-v_nb
#print(z_sub_nb)



##
# Vector multiplication with a scalar
# #

y_np = np.array([1,2])
z_mul_np = 2 * y_np
# print(z_mul_np)


###
# Product of two numpy arrays
# #

x_np = np.array([1,2])
w_np = np.array([3,2])
z_prod_np = x_np * w_np
# print(z_prod_np)

##
# Dot Product
# ##

a1_np = np.array([1,2])
a2_np = np.array([3,2])
z_dot_prod_np = np.dot(a1_np,a2_np)
# print(z_dot_prod_np)


##
# Add Constant to an numpy array (Broadcasting)
# ##

a3_np = np.array([1,2,3,-1])
z_broad_np = a3_np + 1 # Add 1 to all elements in the array
# print(z_broad_np)

###
# Universal function
# ##

x_linespace = np.linspace(-2,2,num=9)
print(x_linespace)



