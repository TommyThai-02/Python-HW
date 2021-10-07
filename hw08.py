#Author: Tommy Thai
#Filename: hw08.py
#Assignment: hw08

def get_vowel(content):
    vowels = "aeiou"

    _numofvowels = 0

    for v in content:
        if v.lower() in vowels:

            _numofvowels += 1
            
    return _numofvowels

def get_consonants(content):
    consonants = "bcdfghjklmpqrstvwxyz"

    _numofconsonants = 0

    for con in content:
        if con.lower() in consonants:

            _numofconsonants += 1

    return _numofconsonants

def get_UpAndLow(content):

    upper = 0
    lower = 0
    
    for uplow in content:
        if uplow.isupper():
            upper += 1
        if uplow.islower():
            lower += 1
    return upper, lower
    
def main():
    try:
        file_name = input("Enter File name: ")
        a = open(file_name, "r")
        content = a.read()
        vowels = get_vowel(content)
        consonants = get_consonants(content)
        upper, lower = get_UpAndLow(content)
        
        print("Vowels:", vowels)
        print("Consonants:", consonants)
        print("Uppercase:", upper)
        print("Lowercase:", lower)
        a.close()
        return content
    except FileNotFoundError:
        print("Error opening file!")
   
main()
    
