# ---------------------------------------------------------
# Wendy Bronson
# Module 9.2 Assignment: APIs
# Date: July 19th 2026
#
# Purpose:
# Connect to An API of Ice and Fire, print the complete
# unformatted response, and display selected character
# information in an easier-to-read format.
#
# Source:
# An API of Ice and Fire
# https://anapioficeandfire.com/
#
# Requests Library Documentation
# https://requests.readthedocs.io/
# ---------------------------------------------------------

import requests


def main():
    """Retrieve and display information about Jon Snow."""

    api_url = (
        "https://www.anapioficeandfire.com/api/characters"
        "?name=Jon%20Snow"
    )

    try:
        # Send a GET request to the API.
        response = requests.get(api_url, timeout=30)

        # Test the connection and display the status code.
        print("Connection status code:", response.status_code)

        # Stop the program if the API returns an error.
        response.raise_for_status()

        # Convert the JSON response into Python data.
        character_data = response.json()

        # Print the complete response without formatting.
        print("\nUnformatted API response:")
        print(character_data)

        # Make sure the API returned at least one character.
        if not character_data:
            print("\nNo character information was found.")
            return

        # Select the first character returned.
        character = character_data[0]

        # Print selected information with formatting.
        print("\nAn API of Ice and Fire Character Information")
        print("--------------------------------------------")
        print("Name:", character["name"])
        print("Gender:", character["gender"])
        print("Culture:", character["culture"])

        # Display aliases.
        print("Aliases:")
        for alias in character["aliases"]:
            if alias:
                print("-", alias)

        # Display titles.
        print("Titles:")
        for title in character["titles"]:
            if title:
                print("-", title)

        # Display television appearances.
        print("TV Series Appearances:")
        for season in character["tvSeries"]:
            if season:
                print("-", season)

        # Display the actor who played the character.
        actors = character["playedBy"]

        if actors and actors[0]:
            print("Played by:", ", ".join(actors))
        else:
            print("Played by: Not listed")

    except requests.exceptions.Timeout:
        print("\nThe API request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("\nThe program could not connect to the API.")
        print("Check your internet connection and try again.")

    except requests.exceptions.RequestException as error:
        print("\nAn error occurred while contacting the API:")
        print(error)


if __name__ == "__main__":
    main()