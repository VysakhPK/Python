import grahics.rectangle as re
import grahics.circle as c
import grahics.trd_graphics.cuboid as cb
import grahics.trd_graphics.sphere as s

print("Rectangle")
print("Area:", re.area(2, 5))
print("Perimeter:", re.perimeter(2, 5))
print("\n")

print("Circle")
print("area:", c.area(4))
print("perimeter:", c.perimeter(4))
print("\n")

print("Cuboid")
print("area:", cb.area(4, 5, 6))
print("perimeter:", cb.perimeter(4, 5, 6))
print("\n")

print("Sphere")
print("area:", s.area(5))
print("perimeter:", s.perimeter(5))
