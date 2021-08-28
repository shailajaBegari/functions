Grosssalary=int(input('enter number:'))
total_savings=int(input("enter number:"))
def taxcalculator():
    remaingsavings=Grosssalary-total_savings
    if remaingsavings<100000:
        print("no tax")
    elif remaingsavings>=100000 or remaingsavings<=200000:
        print(remaingsavings*0.1)
    elif remaingsavings>=200000 or remaingsavings<=500000:
        print(remaingsavings*0.1+remaingsavings*0.2)
    elif remaingsavings>=500000:
        print(remaingsavings*0.1+remaingsavings*0.2+remaingsavings*0.3)
taxcalculator()