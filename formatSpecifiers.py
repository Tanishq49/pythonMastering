# Format Specifiers in Python

# Specifier    Meaning                              Example Output (value = 12.3456)
# -------------------------------------------------------------------------------
# .2f          Fixed-point with 2 decimals           -> 12.35
# d            Integer in decimal                    -> 123
# x            Integer in hexadecimal (lowercase)    -> 7b
# X            Integer in hexadecimal (uppercase)    -> 7B
# e            Scientific notation (lowercase)       -> 1.23e+01
# %            Percentage (multiplies by 100)        -> 1234.56%
# >, <, ^      Align right, left, center             -> Depends on context

monitor_cost = 500.234798
cpu_cost = 5000.234
total_cost = monitor_cost+cpu_cost

#Now using the format specifers..

#Todo: Adding all the format specifier in this print statement
#! If there is error on the github so dont push the code
print(f"Your total bill is ${total_cost:<10,.2f}")