#python as a calculater
print(2+3)  # Addition
print(5-2)  # Subtraction   
print(4*3)  # Multiplication
print(8/2)  # Division
print(7%3)  # Modulus
print(2**3) # Exponentiation
print(7//3) # Floor Division
# Output:
# 5
# 3
# 12
# 4.0
# 1
# 8
# 2
print(2*3.) # Multiplication with float
print(2.*3) # Multiplication with int
print(2.*3.) # Multiplication with float
print(2**3.) # Exponentiation with float
print(2.**3) # Exponentiation with int  
print(2.**3.) # Exponentiation with float
print(7/3.) # Division with float
print(7./3) # Division with int 
print(7./3.) # Division with float
print(7//3.) # Floor Division with float    
print(7./3)  # Floor Division with int
print(7./3.) # Floor Division with float
print(-6//4) # Floor Division with negative numerator
print(6.//-4) # Floor Division with negative denominator
print(-6.//-4) # Floor Division with both negative numerator and denominator    
print(4.+3*2) # Mixed operations with float and int
print((4.+3)*2) # Mixed operations with float and int with parentheses
print(4+3*2.) # Mixed operations with int and float
print((4+3)*2.) # Mixed operations with int and float with parentheses
print(4.+3*2.) # Mixed operations with float
print((4.+3)*2.) # Mixed operations with float with parentheses
print(4//3*2.) # Mixed floor division and multiplication with float and int
print((4//3)*2.) # Mixed floor division and multiplication with float and int with parentheses
print(4.//3*2) # Mixed floor division and multiplication with int and float
print((4.//3)*2) # Mixed floor division and multiplication with int and float with parentheses
print(4.//3*2.) # Mixed floor division and multiplication with float
print((4.//3)*2.) # Mixed floor division and multiplication with float with parentheses


#list of priority of operators in python
# Parentheses ()
# Exponentiation (**)
# Unary operators (+, -, ~)
# Multiplication (*), Division (/), Floor Division (//), Modulus (%)
# Addition (+), Subtraction (-)
# Bitwise AND (&)
# Bitwise XOR (^)
# Bitwise OR (|)
# Comparison operators (==, !=, <, >, <=, >=)
# Identity operators (is, is not)
# Membership operators (in, not in)
# Logical AND (and)
# Logical OR (or)
# Assignment operators (=, +=, -=, *=, /=, %=, **=, //=, etc.)
# Note: Operators with the same precedence level are evaluated from left to right.
# Example to demonstrate operator precedence
result = 3 + 4 * 2 ** 2 / (1 - 5)
print(result)  # Output: -1.0


#operators and parrentheses
a = 10
b = 5
c = 2
result1 = a + b * c  # Without parentheses
result2 = (a + b) * c  # With parentheses
print(result1)  # Output: 20
print(result2)  # Output: 30
# In the first case, multiplication is performed before addition due to operator precedence.
# In the second case, parentheses change the order of operations, so addition is performed first.

print((5*((25%13)+100)/(2*13))//2) # Output: 10.0
# Breakdown of the expression:
# 1. Calculate the modulus: 25 % 13 = 12
# 2. Add 100: 12 + 100 = 112
# 3. Multiply by 5: 5 * 112 = 560   
# 4. Calculate the denominator: 2 * 13 = 26
# 5. Divide the numerator by the denominator: 560 / 26 ≈ 21.53846153846154
# 6. Perform floor division by 2: 21.53846153846154 // 2 = 10.0

"""Section Summary:
In this section, we explored various arithmetic operators in Python, including addition, subtraction, multiplication, division, modulus, exponentiation, and floor division.
We also examined how these operators behave with different data types (integers and floats) and how operator precedence and parentheses affect the order of operations in expressions.
Understanding these concepts is crucial for performing accurate calculations and writing effective code in Python.
 A unary operator is an operator with only one operand, e.g., -1, or +3.
 A binary operator is an operator with two operands, e.g., 4 + 5, or 12 % 5.
  The exponentiation operator uses right-sided binding, e.g., 2 ** 2 ** 3 = 256"""
