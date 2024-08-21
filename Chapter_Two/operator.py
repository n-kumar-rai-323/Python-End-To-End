# Operator in python 

# following are some common operators in python ..
# 1. Arithmetic Operators (Addition + , Subtraction -, Multiplication *, divisions /,floor Division //, Modules %, Exponentiation **  ) 
num =3
numm =4
add = num + numm
sub = num = numm
mul = num * numm
div = num / numm
flor= num // numm
Mod = numm % numm
exp = numm ** numm

# 2. Assignment Operators ( double equal == , addition equal +=, subtraction equal -= )
x += 5  # Equivalent to x = x + 5
x -= 3  # Equivalent to x = x - 3
# 3. Comparison operators(Equal to = , lessthan equal to <=, grater than equal to >-, not equal to !=)
x == y  # True if x is equal to y
x != y  # True if x is not equal to y
x > y  # True if x is greater than y
x < y  # True if x is less than y
x >= y  # True if x is greater than or equal to y
x <= y  # True if x is less than or equal to y

x = 10
y = 20

print(x == y)  # False, because 10 is not equal to 20
print(x != y)  # True, because 10 is not equal to 20
print(x > y)   # False, because 10 is not greater than 20
print(x < y)   # True, because 10 is less than 20
print(x >= 10) # True, because 10 is equal to 10
print(x <= 5)  # False, because 10 is not less than or equal to 5




# 4. logical operators (AND &, OR | , NOT !)
x = 5
y = 10
print(x > 3 and y < 15)  # True, because both conditions are true
print(x > 7 and y < 15)  # False, because the first condition is false


x = 5
y = 10
print(x > 7 or y < 15)  # True, because the second condition is true
print(x > 7 or y > 15)  # False, because both conditions are false


x = 5
print(not x > 7)  # True, because x > 7 is false
print(not x < 7)  # False, because x < 7 is true



x = 5
y = 10

# Using and
if x > 3 and y < 15:
    print("Both conditions are true")

# Using or
if x > 7 or y < 15:
    print("At least one condition is true")

# Using not
if not x > 7:
    print("x is not greater than 7")
