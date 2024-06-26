"""
- Testing out the Exception Handling (i.e. Error handling)
"""
# 1: try = Test code for errors & except = Handles the error
 
x = 23

try:
    print(x)
except NameError:
    print("Variable x is not defined!")
except:
    print("Something else went wrong!?")

# 2: else = executes code if no error

#y = "Hello"

try:
    print("Hi")
except:
    print("Something went wrong!")
else:
    print("Nothing went wrong.")


# 3: finally = executes code regardless of the test (even if errors are there)

try:
    print("z")
except:
    print("Something went wrong!")
finally:
    print("The test is finished!")