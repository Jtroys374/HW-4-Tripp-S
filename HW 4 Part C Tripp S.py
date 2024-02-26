import numpy as np


"""This program was created with the aid of chat gpt
I could not find a partner for this hw as well."""

# Define the coefficient matrices and the constant vectors
A1 = np.array([[3, 1, -1],
               [1, 4, 1],
               [2, 1, 2]])

A2 = np.array([[1, -10, 2, 4],
               [3, 1, 4, 12],
               [9, 2, 3, 4],
               [-1, 2, 7, 3]])

b1 = np.array([2, 12, 10])
b2 = np.array([2, 12, 21, 37])

# Solve the systems of equations
x1 = np.linalg.solve(A1, b1)
x2 = np.linalg.solve(A2, b2)

# Print the solutions
print("Solution to the first system of equations:")
print("x1 = {:.2f}".format(x1[0]))
print("x2 = {:.2f}".format(x1[1]))
print("x3 = {:.2f}".format(x1[2]))

print("\nSolution to the second system of equations:")
print("x1 = {:.2f}".format(x2[0]))
print("x2 = {:.2f}".format(x2[1]))
print("x3 = {:.2f}".format(x2[2]))
print("x4 = {:.2f}".format(x2[3]))
