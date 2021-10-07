#Author: Tommy Thai
#Filename: hw09.py
#Assignment: hw09

import pickle

view = "Vv"
add = "Aa"
change = "Cc"
delete = "Dd"

def _pickle(veggies):
    
    output_file = open("veggies.dat", "wb")
    pickle.dump(veggies, output_file)   
    output_file.close()
    
def _unpickle():
    
    input_file = open("veggies.dat", "rb")
    veggies = pickle.load(input_file)
    input_file.close()
    print("Veggies loaded!")
    print()
    return veggies

def get_choice():

    print()
    print("-=-=- Menu -=-=-")
    print("V. View veggies.")
    print("A. Add new veggie.")
    print("C. Change veggie.")
    print("D. Delete veggie.")
    choice = input("Enter your choice: ")
    print("-=-=-=-=-=-=-=-=-=-=-")
    print()
    return choice

def view_veggies(veggies):
    
    
    print()
    print()
    print("-=-=- Veggie, Price -=-=-")
    for i in veggies:
        print("{},".format(i),veggies[i])
    print()
    print()
    print("-=-=- Goodbye! -=-=-")
    
def add_veggie(veggies):
    
    veggie_name = input("Enter veggie name: ") 
    veggie_price = input("Enter veggie price: ")
    veggies[veggie_name] = veggie_price
    print()
    print()
    print("-=-=- Goodbye! -=-=-")
    
def change_veggie(veggies):
    print("-=-=- Enter New Veggie Name and/or Price -=-=-")
    veggie_name = input("Enter veggie name: ")
    veggie_price = input("Enter veggie price: ")
    veggies[veggie_name] = veggie_price
    print()
    print()
    print("-=-=- Goodbye! -=-=-")
def delete_veggie(veggies):
    veggie_name = input("Enter veggie name: ")
    if veggie_name in veggies:
        del veggies[veggie_name]
        print()
        print()
        print("-=-=- Goodbye! -=-=-")
def main():
    
    try:
        veggies = _unpickle()
        choice = get_choice()
    except FileNotFoundError:
        print("No existing veggies found.")
        print("A new veggies file will be created.")
        veggies = {}
        f = open("veggies.dat", "wb")
        pickle.dump(veggies, f)
        f.close()
        choice = get_choice()

    if choice in view:
            view_veggies(veggies)
    elif choice in add:
            add_veggie(veggies)
    elif choice in change:
            change_veggie(veggies)
    elif choice in delete:
            delete_veggie(veggies)
    
    _pickle(veggies)
    
main()
