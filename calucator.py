def calculator(num1,num2,operator):
    if operator=="addition":
        sum=num1+num2
        return sum
    if operator=="sub":
        sub=num1-num2
        return sub
    if operator=="mul":
        mul=num1*num2
        return mul
    if operator=="div":
        div=num1/num2
        return  div
num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
operator=input("enter you operator'addition/sub/mul':")
print(calculator(num1,num2,operator))
