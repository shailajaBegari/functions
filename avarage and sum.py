def sum_avg(num):
    i=0
    sum=0
    count=0
    while i<3:
        user=int(input("enter the number:"))
        sum=sum+user
        count=count+1
        i+=1
    print(sum)
    print(sum/count)
sum_avg(sum)


