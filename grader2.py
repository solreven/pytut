#Here I'm just gonna comment along what the workshoop actually wants me to do.

# Defines a string variable
name = "Alice"
# Prints the variable
print(name)
# Prints the variable type
print(type(name))
# This suggests that I can sort of safely redeclare this as:
name: str = "Alice"
# But if I refer to name: str, does it understand that that's the original name?
#   I tested this by redeclaring it, and it worked.

# Prints the variable
print(name)
# Prints the variable type
print(type(name))

# Wants a boolean for whether the student is currently enrolled
is_enrolled: bool = True

# Now suggests that I print the boolean type like so:
print(is_enrolled, type(is_enrolled))

# That suggests that I should just print with type hints too!
# print(str(name))
# Copilot says that's just messing around xD
# So I'm guessing the lesson here is:
print("It is", bool(is_enrolled), "that", name, "is currently enrolled.")
# That works.
# Asks for age
age: int = 20
print("It is", bool(age), "that", name, "is currently enrolled and at the age of", str(age))

# It wants me to check the type for score by using isinstance instead of type all of a sudden.
score = 9000.1
print(isinstance(score, int))
# I'm guessing that they're introducing it because a boolean can be used in a function. Type just gives me as the developer more info.
print(type(score))

# Cool, so what I've learned so far is that I can use type hints to make sure others know what type a variable is,
# as well as what type a function takes as a parameter.
# I also know that I can use isinstance to check the type of a variable and throw an error if it's not the right type.