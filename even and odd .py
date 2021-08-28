def show_number(num):
    i=0
    while i<=num:
        if i%2==0:
            print (i,'even')
        else:
            print(i,'odd')
        i=i+1
user=int(input('enter number'))
show_number(user)        
                
