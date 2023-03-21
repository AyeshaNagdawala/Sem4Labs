
a=int(input("enter the first number"))
b=int(input("enter the second number"))
#try : add all exceptional cases here
try:
    c=a/b
#except :show/do this if try statement has an exception
except Exception as e:
    print(e)
#else: if no exception do this
else:
    print(f"Division is {c}")
#finally: regardless of exception the following should happen
finally:
    print("Thank You")



# raising our own exception

class InvaliNum(Exception):
    pass

a=int(input("enter the first number"))
b=int(input("enter the second number"))
#try : add all exceptional cases here
try:
    c=a/b
    if a==4:
        raise InvaliNum 
#except :show/do this if try statement has an exception
except InvaliNum:
    print("Num")
    #print(e)
#else: if no exception do this
else:
    print(f"Division is {c}")
#finally: regardless of exception the following should happen
finally:
    print("Thank You")
