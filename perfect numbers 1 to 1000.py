def perfec_tnumber(num2):
    num=1
    while num<=num2:
        i=1
        sum=0
        while i<num:
            if num%i==0:
                sum=sum+i
            i=i+1
        if sum==num:
            print(num)
        num=num+1
user=int(input('enter number:'))
perfec_tnumber(user)

# perfec_tnumber(100)
# perfec_tnumber(1000)

