from math import acos, pi
import numpy as np
from scipy.optimize import fsolve, least_squares

def acos_safe(x) -> float:
    if -1 <= x and x <= 1:
        return acos(x)
    return -100

def triangle_sides(abc: np.array) -> float:
    a, b, c = abc # represents the three sides
    cosA = (c-b) / (2*b)
    cosB = (a-c) / (2*c)
    cosC = (a+c) / (2*b)
    print(a, b, c)
    return [acos_safe(cosA) + acos_safe(cosB) + acos_safe(cosC) - pi,
            a**2 - b**2 - b*c,
            b**2 - c**2 - a*c,
            b - 1]

# def triangle_angles(abc: np.array) -> float:
#     c_, b_, a_ = abc # represents the three angles
#     cosA = (c-b) / (2*b)
#     cosB = (a-c) / (2*c)
#     cosC = (a+c) / (2*b)
#     return [
#         a**2 - b**2 - b*c,
#         b**2 - c**2 - a*c,
#         acos(cosA) + acos(cosB) + acos(cosC) - pi,
#         # a-1 # smallest side has length 1
#     ]

# a1 = lambda b, c: triangle(1, b, c)
# b1 = lambda a, c: triangle(a, 1, c)
# c1 = lambda a, b: triangle(a, b, 1)

# solve for a == 1, b == 1, or c == 1
# solution = least_squares(triangle_sides, np.array([2, 2, 2]), bounds=((1, 1, 1), (10, 10, 10)), gtol=None, ftol=None, xtol=1e-10)
# print(solution)