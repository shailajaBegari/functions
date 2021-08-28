def  driverspped(speed):
    if speed<70:
        print("ok u r spped is control of u bike")
    else:
        list=[0,70,75,80,85,90,95,100,105,110,115,120,125,130,135]
        i=0
        while i<len(list):
            if list[i]>=speed:
                print("points",i)
                break
            if i>=12:
                print("points  greaterthan 12 licence suspended" )
            i=i+1
user=int(input("enter the speed:-"))
driverspped(user)
                            
