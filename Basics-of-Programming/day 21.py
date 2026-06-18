import time 

#print(time.clock()) is old so no longer used
#print(time.time()) same as print(time.time())

currentTime = time.time()
pastTime = time.time()
print("Hello")
print("World")
print(pastTime - currentTime) #Always will be random 

print("1")
time.sleep(1)
print('2')

#time.sleep(N) first output vanthu ethna seconds kalichi second output varathe determine pannu
#N can be a positive integer or decimal number, zero

for i in range(1,11):
    print(i)
    time.sleep(1)
    
