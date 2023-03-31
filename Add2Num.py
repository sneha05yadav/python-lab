## add two number ##
num1=input("Enter the frist number:")
num2=input("Enter the second number:")
sum=int(num1)+int(num2)
print(sum)
print()

## find the number is negative or postive ##
num=int(input("Enter the number"))
if num>0:
    print("postive number")
else:
    print("negative numbder")
print()

##find the greatest number##
num1=input("Enter the frist number:")
num2=input("Enter the second number:")
num3=input("Enter the third number:")
if(num1>=num2)and(num1>=num3):
    largest=num1
elif(num2>=num1)and(num2>=num3):
    largest=num2
else:
    largest=num3
print("The largest number is", largest)

if(num1<=num2)and(num1<=num3):
    samllest=num1
elif(num2<=num1)and(num2<=num3):
    samllest=num2
else:
    samllest=num3
print("The smallest number is", samllest)
print()

## weak days##
s=int(input("Enter the number"))
if s>7 or s<1:
    print("invalid")
elif s==1:
    print("Sunday")
elif s==2:
    print("Monday")
elif s==3:
    print("Tuesday")
elif s==4:
    print("Webnesday")
elif s==5:
    print("Thursday")
elif s==6:
    print("Firday")
elif s==7:
    print("Saturday")
    

