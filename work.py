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