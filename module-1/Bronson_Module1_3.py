# Wendy Bronson
# 06/07/2026
# Assignment Module 1.3 - 100 Bottles of Beer
# This program counts down bottles of beer on the wall using a function.

# Function that manages the countdown
def countdown_bottles(number_of_bottles):

    # Continue countdown until 1 bottle remains
    while number_of_bottles > 1:

        # Display current bottle count
        print(f"{number_of_bottles} bottles of beer on the wall, "
              f"{number_of_bottles} bottles of beer.")

        print(f"Take one down and pass it around, "
              f"{number_of_bottles - 1} bottle(s) of beer on the wall.\n")

        # Subtract one bottle each loop
        number_of_bottles = number_of_bottles - 1

    # Display final bottle message
    print("1 bottle of beer on the wall, 1 bottle of beer.")

    print("Take one down and pass it around, "
          "0 bottle(s) of beer on the wall.\n")


# Main program

# Ask user for number of bottles
starting_bottles = int(input("Enter number of bottles: "))

# Send value to countdown function
countdown_bottles(starting_bottles)

# Remind user to buy more beer
print("Time to buy more bottles of beer.")