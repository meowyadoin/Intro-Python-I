# Write a function is_even that will return true if the passed-in number is even.


def is_even(n):
    #check if number is divisible by 2 with no remainder
    if n % 2 == 0:
        print("Even!")
        return True
    else:
        print("Odd")
        return False



# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

is_even(num)