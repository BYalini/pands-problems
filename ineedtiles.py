# This program calculate how many  tiles you will need
# when tiling a wall or floor (m2)
length = float(input("Enter room length: "))
width = float(input("Enter room width: "))

area = length * width

needed = area * 1.05

print ("you need", needed, "tiles in meter squires.")
