def area_of_triangle(base, height):
    return 0.5 * base * height
def area_of_sphere(radius):
    return 4/3 * 3.142 * radius**3

base = int(input("Ehter the value of the base: "))
height = int(input("Enter the value of the height: "))
radius = int(input("Enter the value of the radius: "))

triangle_area = area_of_triangle(base, height)
sphere_area = area_of_sphere(radius)

print(f"Area of triangle is {triangle_area}")
print(f"Area of sphere is {sphere_area}")