# def first_function():
#     s = "my name is shailu"
#     def second_function():
#         n = "my hubby name is nani"
#         print(n)     
#     second_function()
#     print(s)    
# first_function() 


def vote(age):
    if age>=18:
        return ('vote is elglible')
    else:
        return("vote is not elgible")
age=int(input('enter the age:'))
print(vote(age))           
