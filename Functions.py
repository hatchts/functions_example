# Conversion Calculator
# By: Stacy Hatch

# User Input regarding length to convert
# Get the Unit from the User
# Convert the Length to the Correcd Unit
# Output Answer to the User

user_number = float(input("What number to convert?"))
user_unit = input("What unit is your number?")

# to convert in to mm --> in x 25.4
# to convert mm to in --> mm / 25.4

# user gives in unit

if(user_unit == 'in'):
    # perform in to mm
    conv_number = user_number * 25.4

elif(user_unit == 'mm'):
    # perform mm to in
    conv_number = user_number / 25.4


print(conv_number)
print(user_unit)