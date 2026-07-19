# ---------------------------------------------------------
# Wendy Bronson
# Module 9 API Assignment
# Date: July 2026
#
# Purpose:
# Test an internet connection and use the Open Notify API
# to display information about people currently in space.
#
# Source:
# Dataquest. How to Use an API in Python.
# Open Notify People in Space API.
# ---------------------------------------------------------

import requests


def main():
    """Test the connection and display current astronaut data."""

    # Test the internet connection.
    connection_response = requests.get(
        "http://www.google.com",
        timeout=10
    )

    print("Connection status code:",
          connection_response.status_code)

    # Request information about people currently in space.
    astronaut_response = requests.get(
        "http://api.open-notify.org/astros.json",
        timeout=10
    )

    # Confirm that the API request was successful.
    print("Astronaut API status code:",
          astronaut_response.status_code)

    # Convert the JSON response to a Python dictionary.
    astronaut_data = astronaut_response.json()

    # Print the response without formatting.
    print("\nUnformatted astronaut response:")
    print(astronaut_data)

    # Print the response with formatting.
    print("\nPeople Currently in Space")
    print("-------------------------")
    print("Total number:", astronaut_data["number"])

    for person in astronaut_data["people"]:
        print(
            person["name"],
            "- Spacecraft:",
            person["craft"]
        )


if __name__ == "__main__":
    main()