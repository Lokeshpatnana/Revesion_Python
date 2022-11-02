# If the condition is satisfied then print statement will be printed,else the condition is not satisfied assertion error will executed.
a = int(input("Enter Your age greater than 18:"))
assert a>=18,"Age is lessthan 18"
print("Your are Eligible for Vote",a)