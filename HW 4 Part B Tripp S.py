import numpy as np
from scipy.optimize import fsolve


"""This program was created with the aid of chat gpt
I could not find a partner for this hw as well."""


# Define the equations
def equation1(x):
    return x - 3 * np.cos(x)


def equation2(x):
    return np.cos(2 * x) * x ** 3


"""The no inspection function below is used since even though there is a warning, the function still works. I've tried
to find out why it gives me errors but i'm chalking it up to magic at this point."""


# Find the roots using fsolve
# noinspection PyTypeChecker
root1 = fsolve(equation1, x0=0)  # initial guess
# noinspection PyTypeChecker
root2 = fsolve(equation2, x0=[-1, 1, 3])  # initial guesses

# Print roots
print("Roots of equation 1: ", root1)
print("Roots of equation 2: ", root2)

# Check if the roots intersect
if len(root1) > 0 and len(root2) > 0:
    intersection_points = np.intersect1d(root1, root2)
    if len(intersection_points) > 0:
        print("The functions intersect at x =", intersection_points)
    else:
        print("The functions do not intersect.")
else:
    print("One or both of the equations have no roots.")
