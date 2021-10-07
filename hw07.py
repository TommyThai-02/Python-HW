#Author: Tommy Thai
#Filename: hw07.py
#Assignment: hw07

num_List = []

def get_Num(num_List):
    
    count = 0

    while count < 10:
        a = int(input("Enter a number for the list: "))
        num_List.append(a)
        count += 1
    return num_List

def get_Total(num_List):
    total = 0
    for num in num_List:
        total += num
    return total

def get_Average():
    total = get_Total(num_List)
    average = total / len(num_List)
    return average
    
def main(num_List):
    get_Num(num_List)
    a = get_Total(num_List)
    b = get_Average()
    print("The lowest number is", min(num_List))
    print("The highest number is", max(num_List))
    print("The total of the list is", a)
    print("The average of the list is", format(b, ".1f"))
    
main(num_List)
