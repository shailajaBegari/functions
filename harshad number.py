def harsadnumber(num2):
    num=1
    while num<=num2:
        temp=num
        sum=0
        while temp>0:
            rem=temp%10
            temp=temp//10
            sum=sum+rem
        if num%sum==0:
            print(num)
        num=num+1
harsadnumber(1000)

