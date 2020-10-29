# first attempt

import math

def roots(a, b, c):
    if b * b - 4 * a * c < 0:
        print("Solution has no real roots.")
    elif b * b - 4 * a * c == 0:
        x = -b / ( 2 * a)
        print("x =", x)
    else:
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
        print("x1 =", x1)
        print("x2 =", x2)