# File:        hw2.py
# Written by:  Kyle Fritz
# Date:        9/19/2013
# Lab Section: 10
############### USE WITH PYTHON 3 ###########
# scl enable python33 bash
# Description: This program adds, subtracts, multiplies, and divides any two
#    numbers (besides division by zero).
print("This program will add, subtract, multiply, or divide any two integers.")
def main():
    int1 = (input("Type in your first operand: "))
    int2 = (input("Type in your second operand: "))
    operAtion = (input("Enter your operation: "))
    a = int(int1)  # This casts the first operand as an integer.
    b = int(int2)  # This casts the second operand as an integer.
    print("The first operand is", a)
    print("The second operand is", b)
    print("The operation that you want to use is:", operAtion)
    if operAtion.lower() == "add":    # This adds both integers.
      print("When you add", int1, "and", int2, "you get", a+b)
      if a+b >= 100 or a+b <= -100:   # This tells the user if his/her result
      # has 3 or more digits in it.
        print("Your result contains 3 or more digits")
    elif operAtion.lower() == "subtract":   # This subtracts the second typed
    # integer from the first one.
      print("When you subtract", a, "and", b, "you get", a-b)
      if a-b >= 100 or a-b <= -100:   # This tells the user if his/her result
      # has 3 or more digits in it.
        print("Your result contains 3 or more digits")
    elif operAtion.lower() == "multiply":  # This multiplies both integers.
      print("When you multiply", a, "and", b, "you get", a*b)
      if a*b >= 100 or a*b <= -100:   # This tells the user if his/her result
      # has 3 or more digits in it.
        print("Your result contains 3 or more digits")
    elif operAtion.lower() == "divide" and b!=0:   # This divides the first
    # integer by the second.
      print("When you divide", a, "by", b, "you get", a/b)
      if a/b >= 100 or a/b <= -100:   # This tells the user if his/her result
      # has 3 or more digits in it.
        print("Your result contains 3 or more digits")
    elif operAtion.lower() in ['divide'] and b==0:  # This makes sure that the
    # user doesn't divide by zero.
      print("You can't divide by zero.")
    else:              # This makes sure that a proper operation was typed in.
      print("Invalid operation.")

    if a>=0 and  b>=0:    # This tells the user whether both of their integers
    # were positive.
      print("Both of your operands were positive.")
    elif a<0 and b<0:     # This tells the user whether both of their integers
    # were negative.
      print("Both of your operands were negative.")

main()
