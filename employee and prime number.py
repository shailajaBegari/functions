 
def employee(name,salary=20000):
        print(name,"your salary is:-",salary)
        
employee("kartik",30000)
employee("deepak")
employee("Goutham",50000)


def primeorNot(num):     
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(num,"times",num//i,"is")
            else:
                print(num,"is a prime number")
                break
    else:
           print(num,"is not a prime number")
primeorNot(51)