#Author: Tommy Thai
#Filename: hw10.py
#Assignment: hw10

class Employee:
    def __init__(self):
        self.__name = ""
        self.__number = ""

    def set_name(self, n):
        self.__name = n

    def get_name(self):
        return self.__name

    def set_number(self, n):
        self.__number = n

    def get_number(self):
        return self.__number

class ProductionWorker(Employee):
    def __init__(self):
        self.__shift_number = 1
        self.__pay_rate = 0.00
       
    def set_shift_number(self, s):
        self.__shift_number = int(s)

    def get_shift_number(self):
        return self.__shift_number

    def set_pay_rate(self, p):
        self.__pay_rate = float(p)

    def get_pay_rate(self):
        return self.__pay_rate


def main():

    workerName = input("Enter the worker's name: ")
    workerNum = input("Enter the worker's number: ")
    payRate = input("Enter the worker's pay rate: ")
    shiftNum = input("Enter the worker's shift number: ")

    worker = ProductionWorker()
    worker.set_name(workerName)
    worker.set_number(workerNum)
    worker.set_pay_rate(payRate)
    worker.set_shift_number(shiftNum)
    

    print("WORKER INFORMATION:")
    print("Name:         ", worker.get_name())
    print("Number:       ", worker.get_number())
    print("Pay Rate:     ", worker.get_pay_rate())
    print("Shift Number: ", worker.get_shift_number())

    

main()






























    
