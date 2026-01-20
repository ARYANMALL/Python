print("The itsy bitsy spider\nclimbed up the waterspout.")    #The letter n placed after the backslash comes from the word newline.
print()                                                      #This prints an empty line.
print("Down came the rain\nand washed the spider out.")



#Using multiple arguments
print("Out come the sun", "and drived away the rain.")      #Multiple arguments are separated by commas.

# Positional arguments
print("My name is", "Python.")
print("Monty Python.")




#Keyword arguments
#seprator
print("My name is", "Python.", sep="---")                   #The sep keyword argument changes the separator between multiple arguments.
print("My name is", "Python.", sep="***")
print("My name is", "Python.", sep="   ")                     #Using spaces as a separator.
print("My", "name", "is", "Python.", sep="")            #Using an empty string as a separator.






#ending
print("Monty Python.", end="!!!\n")                          #The end keyword argument changes what is printed at the end of the output. The default is a newline character (\n).
print("Monty Python.", end="***\n")
print("Monty Python.", end="   \n")                           #Using spaces before the newline.                              
print("My name is", end="")
print(" Python.")                    #Continuing on the same line.



#Combining positional and keyword arguments
print("My name is", "Python.", sep="---", end="!!!\n")
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print("Hello, World!")
print("Hello, World!")



#  LAB   The print() function and its arguments
print("Programming","Essentials","in", sep="***", end="...")
print("Python")
print("is","fun!", sep="---")



#   LAB   Formatting the output
# Sample 
###################
print("original version:")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
###################
print("with fewer 'print()' invocations:") 
###################
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
###################
print("higher:")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
###################
print("doubled:")
###################
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)
###################
print("tripled:")
###################
print("        *        "*3) 
print("       * *       "*3)
print("      *   *      "*3)
print("     *     *     "*3)
print("    *       *    "*3) 
print("   *         *   "*3)
print("  *           *  "*3)
print(" *             * "*3)
print("******     ******"*3)
print("     *     *     "*3)
print("     *     *     "*3)
print("     *     *     "*3)
print("     *     *     "*3)
print("     *     *     "*3)
print("     *     *     "*3)
print("     *******     "*3)


# Literals – the data in itself
print("123")
print(123)
print("123.45")
print(123.45)
print(True)

#Octal and hexadecimal numbers
print(0o123)      #Octal literal
print(0x123)      #Hexadecimal literal

#floats
print(1.23e2)     #Scientific notation for 1.23 × 10^2
print(1.23e-2)    #Scientific notation for 1.23 × 10^-2
print(0.000123)   #Decimal float
print(.123)       #Decimal float without leading zero
print(123.)       #Decimal float without trailing zero
print(123.0)      #Decimal float with trailing zero
print(0.)         #Decimal float zero without trailing zero
print(.0)         #Decimal float zero without leading zero
print(0.0)        #Decimal float zero with leading and trailing zero
print(True)       #Boolean literal for true
print(False)      #Boolean literal for false

#Ints vs. floats
print(5)          #Integer literal
print(5.0)        #Float literal


#Integer and float literals in expressions

print(5 + 0.0)    #Integer added to float results in float
print(5 / 2)      #Division results in float
print(5 // 2)     #Floor division results in integer........floor division is a mathematical operation that divides two numbers and rounds the result down to the nearest whole number (integer)
print(5 * 2.0)    #Integer multiplied by float results in float
print(5 - 2.0)    #Integer minus float results in float
print(5 ** 2.0)   #Integer exponentiated by float results in float
print(5 % 2.0)    #Integer modulo float results in float

#Type checking with type()

print(type(5))     #Type of integer literal
print(type(5.0))   #Type of float literal
print(type(5 + 0.0)) #Type of integer added to float
print(type(5 / 2))   #Type of division result
print(type(5 // 2))  #Type of floor division result
print(type(5 * 2.0)) #Type of integer multiplied by float
print(type(5 - 2.0)) #Type of integer minus float
print(type(5 ** 2.0))#Type of integer exponentiated by float
print(type(5 % 2.0)) #Type of integer modulo float
print(type(True))    #Type of boolean literal True
print(type(False))   #Type of boolean literal False


#Boolean literals in expressions

print(True + 1)     #Boolean True treated as integer 1
print(False + 1)    #Boolean False treated as integer 0
#Type checking for boolean literals in expressions
print(type(True + 1))  #Type of boolean True treated as integer 1
print(type(False + 1)) #Type of boolean False treated as integer 0


#Float literals

print(3E8)        #Scientific notation for 3 × 10^8
print(0.0000003)  #Decimal float
print(.3e-6)      #Scientific notation for 3 × 10^-7
print(300000000.0)#Decimal float with trailing zero
print(300000000.) #Decimal float without trailing zero

#Type checking for float literals

print(type(3E8))        #Type of scientific notation float
print(type(0.0000003))  #Type of decimal float
print(type(.3e-6))      #Type of scientific notation float
print(type(300000000.0))#Type of decimal float with trailing zero
print(type(300000000.)) #Type of decimal float without trailing zero


#Binary, octal, and hexadecimal literals
print(0b1010)     #Binary literal for 10
print(0o12)      #Octal literal for 10
print(0xA)       #Hexadecimal literal for 10

#Type checking for binary, octal, and hexadecimal literals

print(type(0b1010))  #Type of binary literal
print(type(0o12))     #Type of octal literal
print(type(0xA))      #Type of hexadecimal literal


#Binary, octal, and hexadecimal literals in expressions
print(0b1010 + 5)   #Binary literal added to integer
print(0o12 + 5)    #Octal literal added to integer
print(0xA + 5)     #Hexadecimal literal added to integer

#Type checking for binary, octal, and hexadecimal literals in expressions

print(type(0b1010 + 5)) #Type of binary literal added to integer
print(type(0o12 + 5))    #Type of octal literal added to integer
print(type(0xA + 5))     #Type of hexadecimal literal added to integer

#Underscores in numeric literals
print(1_000_000)        #Integer literal with underscores
print(1_000_000.0)      #Float literal with underscores 
print(1_000_000 + 0.0)  #Integer with underscores added to float
print(1_000_000 / 2)    #Integer with underscores divided by integer

#Type checking for numeric literals with underscores

print(type(1_000_000))      #Type of integer literal with underscores
print(type(1_000_000.0))    #Type of float literal with underscores
print(type(1_000_000 + 0.0))#Type of integer with underscores added to float
print(type(1_000_000 / 2))  #Type of integer with underscores divided by integer


#String literals
print("Hello" "World")    #String literals placed next to each other are concatenated.
print("Hello" + "World")  #String literals concatenated with + operator.
print("Hello" * 3)        #String literal repeated with * operator.

#Type checking for string literals

print(type("Hello" "World"))  #Type of concatenated string literals.
print(type("Hello" + "World"))#Type of concatenated string literals with + operator.
print(type("Hello" * 3))      #Type of repeated string literal.


#Escape characters in string literals
print('Hello\nWorld')      #String literal with newline escape character.
print("Hello\tWorld")      #String literal with tab escape character.
print('It\'s a beautiful day!') #String literal with escaped single quote.
print("He said, \"Hello!\"")    #String literal with escaped double quotes.

#Type checking for string literals with escape characters

print(type('Hello\nWorld'))      #Type of string literal with newline escape character.
print(type("Hello\tWorld"))      #Type of string literal with tab escape character.
print(type('It\'s a beautiful day!')) #Type of string literal with escaped single quote.
print(type("He said, \"Hello!\""))    #Type of string literal with escaped double quotes.


#Multi-line string literals
print("""This is a
multi-line  string.""")          #Multi-line string literal using triple double quotes.
print('''This is another
multi-line string.''')        #Multi-line string literal using triple single quotes.

#Type checking for multi-line string literals

print(type("""This is a
multi-line  string."""))          #Type of multi-line string literal using triple double quotes.
print(type('''This is another 
multi-line string.'''))        #Type of multi-line string literal using triple single quotes.   


#The None literal
print(None)               #The None literal represents the absence of a value.

#Type checking for the None literal

print(type(None))         #Type of the None literal.


#Coding floats
print(0.1 + 0.2)          #Adding two float literals.
print(0.3)                 #A float literal.
print(0.1 + 0.2 == 0.3)    #Checking for equality between the sum of two float literals and another float literal.




"""Section Summary (Simplified)
1. 	Literals → Fixed values in code (e.g., , ).
2. 	Number Systems → Binary (base 2: 0,1), Octal (base 8), Hexadecimal (base 16: 0–9, A–F).
3. 	Integers → Whole numbers, positive or negative (e.g., , ).
4. 	Floats → Numbers with fractions (e.g., ).
5. 	Strings → Use escape () or opposite quotes to include  or .
6. 	Booleans →  (1) and  (0).
7. 	None → Special literal for "no value"."""



