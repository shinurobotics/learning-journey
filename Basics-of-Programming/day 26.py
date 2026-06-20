#float("123.4") -> 123.4
#float("N/A") -> error

#General form
#try:

#except:

#Form 1
try:
    print(int("Hello")) 
except:
    print("Entered exception")
print("Past exception")

#Form 2
keyword = "123"
try:
    print(int(keyword))
except:
    print("Entered exception")
print("Past exception")

#Form 3
try:
    print(int("Visnu"))
except:
    pass
print("Past exception")

#Form 4
key = "Hello"
try:
    print(int(key))
except ValueError: # or except Exception as e:
    print("got a ValueError")
except:
    print("Other type of exception")
finally:
    print("Finally")
print("Past exception")

try:
    raise NameError
except ValueError:
    print("got a ValueError")
except:
    print("Other type of exception")
    raise

finally:
    print("Finally")
print("Past exception")
