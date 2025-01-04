import time# take the number as input
number = int(input())
#use a while loop for the countdown
number = number + 1
for i in range (number):
    print (number-i-1) 
    time.sleep(1)
