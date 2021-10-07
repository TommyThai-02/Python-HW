#Author: Tommy Thai
#Filename: hw12.py
#Assignment: hw12

# Set up recursion
def count_down_by_2(n):
    
    # if statement will end the recursion statement once the integer reaches zero
    # or one for odd integers
    # print statement will print each value
    # recursion statement counts down by 2 from the integer
    
    if n >= 0:
        print(n)
        count_down_by_2(n-2)

# Pass a positive integer here using variable "num", (any positive number)
# if the integer is odd it should stop at 1
# if the integer is even it should stop at 0
# Change the integer by changing the variable "num"

def main():
    num = 13 
    print("Calling function, passing it {}:".format(num))
    count_down_by_2(num)

main()
