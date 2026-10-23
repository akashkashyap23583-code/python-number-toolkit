while True :
    print("\n")
    print("============================================")
    print("              PYTHON NUMBER TOOLKIT      ")
    print("============================================")
    print("1. Multiplication Table")
    print("2. Sum of Numbers")
    print("3. Factorial")
    print("4. Fibonacci Series")
    print("5. Prime Number Checker")
    print("6. Armstrong Number Checker")
    print("7. Palindrome Checker")
    print("8. Reverse a Number")
    print("9. Sum of Digits")
    print("10. Pattern Printing")
    print("11. Exit")

    num = int(input("Enter your choose : "))
    if(num == 11):
        print("\n")
        break

    elif(num > 11):
        print("\n")
        print("Not a valid chooce ! ")

        
    elif(num == 10):
        print("\n")
        n = int(input("Enter the number of rows : "))
        for i in range(n):
            for j in range(i):
                print("*", end=" ")
            print()


    elif(num == 9):
        print("\n")
        n = int(input("Enter the number : "))
        total = 0
        while n != 0 :
            digit = n % 10
            total = total + digit
            n = n // 10
        print("\nSum of digits : ",total)


    elif(num == 8):
        print("\n")
        n = int(input("Enter the number : "))
        reverse = 0
        while n != 0 :
            digit = n % 10
            reverse = reverse * 10 
            reverse =  reverse + digit
            n = n // 10
        print("\nReverse number is : ",reverse)



    elif(num == 7):
            print("\n")
            n = int(input("Enter the number : "))
            chek = n
            reverse = 0
            while n != 0 :
                digit = n % 10
                reverse = reverse * 10
                reverse =  reverse + digit
                n = n // 10
            if(chek == reverse):
                print("Polindrome ! ")
            else :
                print("Not Polindrome !")


    elif(num == 6):
            print("\n")
            n = int(input("Enetr your number : "))
            power = len(str(n))
            copy = n
            total = 0
            while n != 0:
                digit = n % 10
                total = total +  digit ** power
                n = n // 10
            if(total == copy):
                print("Number is Armstrong")
            else :
                print("Not Armstromg")
                            


    elif(num == 5):
        print("\n")
        n = int(input("Enetr your Number : "))
        point = 0
        if(n > 0):
            for i in range(1 ,n + 1):
                if(n % i == 0):
                    point = point + 1
        
        
            if(point ==  2):
                print("Prime Number ")
        
            else :
                print("Not a prime Number ")
        else :
            print("Enter only Possitive Number")
        

    elif(num == 4):
        print("\n")
        n = int(input("Enter Number :"))
        a = 0
        b = 1
        for i in range(0,n):
            print(a,end=" ")
            c = b + a
            a = b
            b = c




    elif(num == 3):
        print("\n")
        n = int(input("Enter your Number : "))
        fact = 1
        if(n > 0):
            for i in range(n, 0,-1):
                fact = i * fact
            print("Factorial : ",fact)
        
        else :
            print("Enter only positive number ")
        


    elif(num == 2): 
        print("\n")

        a = int(input("Enter your first number : "))
        b = int(input("Enter your seccond  number : "))

        total = a + b

        print("\nSum : ",total)


    elif(num == 1):
        print("\n")

        n = int(input("Enter your Number : "))
        print("\n")
        for i in range(1 ,11):
            print(n," X ",i, " = ",i * n)
        
    else :
        print("Check your ptogram ")
        print("Thank You")
        
