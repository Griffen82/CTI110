#Michael Urbi
#Febuary 18, 2025
#P2Lab1
#Using Python to calculate the diameter, circumference, and area of a circle

import math

pi = math.pi

rad = float(input("What is the radius of the circle? ",))

print("")

dia = 2*rad

cir = 2*pi*rad

area = pi*(pow(rad, 2))

print("The diameter of the circle is", f"{dia:.1f}", "\n")

print("The circumference of the circle is", f"{cir:.2f}", "\n")

print("The area of the circle is", f"{area:.3f}")
