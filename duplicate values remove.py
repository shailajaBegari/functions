# def dublicate(n):
#     i=0
#     b=[]
#     while i<len(n):
#         if n[i] not in b:
#             b.append(n[i])
#         i=i+1
#     print(b)
# n=["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"] 
# dublicate(n)


def asending(n):
    i=0
    b=[]
    while i<len(n):
        n=n2+n1
        n.sort()
        if  n[i] not in b:
            b.append(n[i])
        i=i+1
    print(b)  
n2=[1, 5, 10, 12, 16, 20]
n1=[1, 2, 10, 13, 16]
asending(n2) 
