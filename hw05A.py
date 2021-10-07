#Author: Tommy Thai
#Filename: hw05A.py
#Assignment: hw05A

def get_score ():
    score = float(input("Enter a score: "))
    while (score < 0 or score > 100):
        print("Invalid score.")
        score = float(input("Try again: "))
    return score    

def main():
    score1 = get_score()
    score2 = get_score()
    score3 = get_score()
    average = (score1 + score2 + score3)/3
    print("Your average:", format(average, ".1f"))
    if (average < 60):
        print("Your grade: F")
    elif (average < 70):
        print("Your grade: D")
    elif (average < 80):
        print("Your grade: C")
    elif (average < 90):
        print("Your grade: B")
    elif (average <= 100):
        print("Your grade: A")

main()
