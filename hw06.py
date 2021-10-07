#Author: Tommy Thai
#Filename: hw06.py
#Assignment: hw06

def get_file_name():
    file_name = str(input("Enter File name: "))
    return file_name

def top(file_name):
    count = 1
    try:
        content = open(file_name, "r")
        while  count != 11:
            inside = content.readline()
            print("{:>2}. {}".format(count, inside.rstrip("\n")),)
            count += 1
    except IOError:
        print("FILE NOT FOUND ERROR:", file_name)
def main():
    file_name = get_file_name()
    top(file_name)
main()



