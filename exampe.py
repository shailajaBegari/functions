
def sum():
    # c=a+b
    print(3+8)
sum() 

def welcome():
    print("Welcome to function")
welcome() 


def isEven():
    if(12%2==0):
        print("Even Number")
    else:
        print("Old Number") 
isEven()


# def add(a,b,c):
#     return (a+b+c)
# print (add(a=8,b=8,c=4))

#Output:SyntaxError: positional argument follows keyword 

def fn(**a):
    for i in a.items():
        print (i)
fn(numbers=5,colors="blue",fruits="apple")

# '''
# Output:
# ('numbers', 5)
# ('colors', 'blue')
# ('fruits', 'apple')
# '''