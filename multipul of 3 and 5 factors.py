def factors(num):
    i=0
    sum=0
    while i<=num:
        if i%3==0 or i%5==0:
            sum=sum+i
            print(i)
        i=i+1  
    print("sum is",sum)
user=int(input('enter number:'))
factors(user)          



