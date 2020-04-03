# This program calculates Body Mass Index (BMI) of a person
# The user inputs are weight in Kg and height in cm

Weight = float(input ("Enter weight in Kg :"))
Height = float(input("Enter Height in cm :"))

# The formula for BMI is weight in kilograms divided by height in meters squared
BMI = Weight / ((Height/100) ** 2)

print ("BMI is", round(BMI,2))

