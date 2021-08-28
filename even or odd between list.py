def check_number(num1,num2):
    if num1%2==0 and num2%2==0:
        return ("two numbers are even")
    else:
        return("two numbers are odd")
def check_number_list(list1,list2):
    i=0
    while i<len(list1):
        j=i
        while j<len(list2):
            print(check_number(list1[i],list2[j]))
            break
            j+=1
        i+=1
list1=[2, 6, 18, 10, 3, 75] 
list2=[6, 9, 24, 12, 3, 87]
print(check_number_list(list1,list2)) 