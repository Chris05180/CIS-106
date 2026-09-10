# Christopher Hernandez M3P5 9/9/26

circle_radius = float(input("Enter radius of circle: "))
# Input the radius of the circle

pi = 3.14
# Input pi to the nearest hundredth

area = pi * (circle_radius * circle_radius)
# Multiply pi by the squared radius which is done by multiplying the radius by the radius

perimeter = 2 * pi * circle_radius
# Multiply 2 by pi and by the radius

print(f"Area={area:7.2f}")
# Display the area of the circle

print(f"Perimeter={perimeter:6.2f}")
# Display the perimeter of the circle