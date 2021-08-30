"""A program to test the effectiveness of relational operators."""

__author__ = "730402712"


first_number: int = int(input("Left-hand side: "))
second_number: int = int(input("Right-hand side: "))
print(str(first_number) + " < " + str(second_number) + " is " + str(first_number < second_number))
print(str(first_number) + " >= " + str(second_number) + " is " + str(first_number >= second_number))
print(str(first_number) + " == " + str(second_number) + " is " + str(first_number == second_number))
print(str(first_number) + " != " + str(second_number) + " is " + str(first_number != second_number))
