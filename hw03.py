#Author: Tommy Thai
#Filename: hw03.py
#Assignment#: hw03

#Prompt user for hieght and weight

height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))

#Plug height and weight into BMI equation

BMI = weight * 703 / (height ** 2)

#Print the user's BMI

print("Your BMI: ", format(BMI, ".2f"))

#Put BMI into a if statement to find the range

if (BMI >= 18.5 and BMI <= 25):
    print("You're at optimal weight!")
elif (BMI > 25):
    print("You're overweight!")
elif (BMI < 18):
    print("You're underweight!")
