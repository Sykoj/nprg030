from point import Point

p1 = Point(2,2)
p2 = Point(1,2)

# test equality
print(p1 == p2)
print(p1 != p2)

# string representation: Point(x,y)
print(p1)

# operations
print(p1 + p2)
print(p1.euclidean_norm())
