

def lenfunction():
    user1=int(input("enter lenth:"))
    i=0
    b=[]
    c=[]
    while i<user1:
        list1=int(input("enter number:"))
        list2=int(input("enter number:"))
        b.append(list1)
        c.append(list2)
        j=0
        d=[]
        while j<=i:
            d.append(b[j]+c[j])
            j=j+1
        i=i+1
    print(d)
lenfunction()

