## ---------------------------------------------------------
# Wendy Bronson
# Module 4.2 Assignment: High/Low Temperatures
# Date: June 2026
#
# Purpose:
# Read weather data from a CSV file and allow the user
# to display either the daily high temperatures,
# daily low temperatures, or exit the program.
#
# Original source:
# sitka_highs.py provided with course materials.
# Modified by Wendy Bronson.
# ---------------------------------------------------------

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

# Read the weather data from the CSV file.
filename = 'Sitka Weather 2018 Data.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Create empty lists.
    dates = []
    highs = []
    lows = []

    # Read each row from the CSV file.
    for row in reader:
        current_date = datetime.strptime(row[2], '%m/%d/%Y')
        high = int(row[5])
        low = int(row[6])

        dates.append(current_date)
        highs.append(high)
        lows.append(low)


# Function to display the high temperature graph.
def display_highs():
    fig, ax = plt.subplots()

    ax.plot(dates, highs, c='red')

    plt.title("Daily High Temperatures - 2018", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


# Function to display the low temperature graph.
def display_lows():
    fig, ax = plt.subplots()

    ax.plot(dates, lows, c='blue')

    plt.title("Daily Low Temperatures - 2018", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


# Display menu instructions.
print("--------------------------------------------")
print(" Sitka Weather Temperature Viewer")
print("--------------------------------------------")
print("H - Display High Temperatures")
print("L - Display Low Temperatures")
print("E - Exit")
print("--------------------------------------------")


# Continue showing the menu until the user exits.
while True:

    choice = input("\nEnter your choice (H, L, or E): ").upper()

    if choice == "H":
        display_highs()

    elif choice == "L":
        display_lows()

    elif choice == "E":
        print("\nThank you for using the Sitka Weather Viewer.")
        print("Program exiting...")
        sys.exit()

    else:
        print("\nInvalid selection. Please enter H, L, or E.")