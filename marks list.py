
def markslist(mark):
    if mark>=91 and mark<=100:
        print("grade A")
    elif mark>=81 and mark<=90:
        print("grade B")
    elif mark>=71 and mark<=80:
        print("grade C")
    elif mark>=61 and mark<=70:
        print("grade D ")
    elif mark>=40 and mark<=50:
        print("grade E")
    else:
        print(" FAIL")
user=int(input('enter number:'))
markslist(user)