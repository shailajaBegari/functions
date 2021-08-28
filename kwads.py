def fn(**a):
    for i in a.items():
        print (i)
fn(numbers=5,colors="blue",fruits="apple")

def add(*b):
    result=0
    for i in b:
        result=result+i
    return result
print (add(1,2,3,4))


