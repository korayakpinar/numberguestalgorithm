import random

while(True):
        num1 = input("Please enter a number between 25 and 0:") 
        if num1.isdigit() == False:
            print("Sayı gir köle!")
            continue
            pass
        enteredNumber = int(num1)
        if enteredNumber < 0 or enteredNumber >= 25:
            print("Number must be between 25 and 0")
            continue
            pass
        a = 0
        num2 = random.randrange(0,25)
        while num2 != enteredNumber:
            num2 = random.randrange(0,25)
            a = a+1
            print(num2)
        
        print(a,"time guess were made.")
        if enteredNumber == num2:
            print("Your entered number:" + num1)
            break
            pass
        pass
