# Wendy Bronson
# June 10, 2026
# CSD-325 Module 2.2 - Documented Debugging
# Purpose: Calculate the average of three test scores.

def calculate_average(score1, score2, score3):
    """Calculate and return the average of three scores."""

    average = (score1 + score2 + score3) / 3
    return average


# Gather scores from the user.
score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))

# Call the function and store the result.
average_score = calculate_average(score1, score2, score3)

# Display the average score.
print(f"The average score is {average_score:.2f}")