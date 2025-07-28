#otp generate using random

import random

otp=random.randint(1000,9999)
print(otp)

attempts=0

while attempts<=3:
        user_otp=int(input("enter the otp:"))
        if len(str(user_otp))!=4:
            print("otp must be 4 digits")
            
        if user_otp==otp:
            print("otp successfully entered") 
            break
        attempts+=1
        if attempts==3:
            print("maximum attempts done ,try after 24 hours")  
            break
