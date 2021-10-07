#Author: Tommy Thai
#Filename: hw04.py
#Assignment: hw04

#Prompt User for number of rows
rows = int(input("Enter the number of rows:"))

#input validation

while rows < 1:
    #Error message
    print("Number of rows must be positive.")
    #Prompt again
    rows = int(input("Enter the number of rows:"))

#After valid input, start loop for printing stars.
while rows > 0:
    columns = rows
    while columns > 0:
        print("*", end = "")
        columns -= 1
    rows -= 1
    print()
