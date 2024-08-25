print("Select an operation to perform: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
option=int(input("Choose an operation: "))
result=0 

if(option in [1,2,3,4]):
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))

    if(option==1):
        result=num1+num2
    elif(option==2):
        result=num1-num2
    elif(option==3):
        result=num1*num2
    elif(option==4):
        result=num1/num2

else:
    print("Invalid operation number")


print("The result of the operation is {}".format(result))