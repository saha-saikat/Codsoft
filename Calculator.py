print("-----Simple Calculator-----")

num1 =float(input("Enter the first number here : "))

num2 =float(input("Enter the second number here : "))

print("Press 1 for Addition\nPress 2 for Subtraction\nPress 3 for Multiplecation\nPress 4 for Divison")

choice=int(input("Press your choice from 1-4:  "))

if choice==1:
    sum=num1+num2
    print("ADDITION OF TWO NUMBER IS:",sum)
elif choice==2:
    sub = num1 - num2
    print("DIFFERENCE OF TWO NUMBER IS:", sub)

elif choice==3:
    mul = num1 * num2
    print("MULTIPLECATION OF TWO NUMBER IS:",mul)

elif choice==4:
    div = num1 / num2
    print("DIVISON OF TWO NUMBER IS:", div)

else:
    print("NUMBER IS INVALID")

