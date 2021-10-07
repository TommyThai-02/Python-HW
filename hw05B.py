#Author: Tommy Thai
#Filename: hw05B.py
#Assignment: hw05B

def get_cost():
    cost = float(input("Enter cost of meal: "))
    while (cost < 0):
        print("Invalid Cost:")
        cost = float(input("Enter cost of meal: "))
    return cost

def compute_tip(cost):
    tip = cost * .18
    return tip

def compute_tax(cost):
    tax = cost * .0825
    return tax

def compute_grand_total(cost, tip, tax):
    total = cost + tip + tax
    return total

def display_total_cost(cost, tip, tax, total):
    
    print()
    print()
    print("Cost:    $ ", format(cost, ".2f"))
    print("Tip:     $ ", format(tip, ".2f"))
    print("Tax:     $ ", format(tax, ".2f"))
    print("Total:   $ ", format(total, ".2f"))

def main():
    cost = get_cost()
    tip = compute_tip(cost)
    tax = compute_tax(cost)
    total = compute_grand_total(cost, tip, tax)
    display_total_cost(cost, tip, tax, total)

main()

