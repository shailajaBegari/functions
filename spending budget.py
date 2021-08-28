def spendingbudget(num):
    if num<=50000:
        print("spending budget is inside")
    else:
        print("spending budget is outside")
amount=int(input('enter number:'))
total=int(input('enter number:'))
spendingbudget(amount*total)            
