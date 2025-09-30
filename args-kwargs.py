# args-kwargs.py

# --- *args: Positional Variable-Length Arguments ---
# The *args syntax allows a function to accept any number of positional arguments.
# 'args' will be a tuple containing all the arguments passed.
def add(*args):
    # This would print the second argument passed to the function (e.g., 5 if called with add(3, 5, 6))
    # print(args[1])

    # Initialize a variable to store the sum.
    sum_total = 0
    # Iterate through the tuple of arguments.
    for n in args:
        sum_total += n
    return sum_total

# Example call to the add function with multiple arguments.
# print(add(3, 5, 6, 2, 1, 7, 4, 3))


# --- **kwargs: Keyworded Variable-Length Arguments ---
# The **kwargs syntax allows a function to accept any number of keyword arguments.
# 'kwargs' will be a dictionary containing all the keyword arguments passed.
def calculate(n, **kwargs):
    # Prints the dictionary of keyword arguments.
    # e.g., {'add': 3, 'multiply': 5}
    print(kwargs)
    
    # You can iterate through the kwargs dictionary like this:
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    
    # Access values from the kwargs dictionary using their keys.
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)

# Call the function with a required positional argument (n=2) and two keyword arguments.
calculate(2, add=3, multiply=5)


# --- How to use a **kwargs dictionary safely in a Class ---
class Car:
    # The __init__ method accepts any number of keyword arguments.
    def __init__(self, **kw):
        # The .get() method is a safe way to access a dictionary key.
        # If the key ("make") exists, it returns its value.
        # If the key does not exist, it returns None instead of raising a KeyError.
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

# Create an instance of the Car class.
# We are providing 'make' and 'model'. 'colour' and 'seats' will be None.
my_car = Car(make="Nissan", model="Skyline")
# Accessing an attribute that was set.
print(my_car.model)
# Accessing an attribute that was not provided will not cause an error.
# print(my_car.colour) # This would print 'None'