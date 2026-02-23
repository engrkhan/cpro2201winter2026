"""
ui.py

This module is the User Interface (UI) layer.

It handles:
- User input
- Display formatting
- Calling database functions
"""

import db
from objects import Movie


def display_welcome():
    """
    Display welcome message when program starts.
    """
    print("The Movie List program")
    print()
    display_menu()


def display_menu():
    """
    Display command options to the user.
    """
    print("COMMAND MENU")
    print("cat  - View movies by category")
    print("year - View movies by year")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")
    print()


def display_categories():
    """
    Display all categories.
    """
    print("CATEGORIES")

    categories = db.get_categories()

    for category in categories:
        print(f"{category.id}. {category.name}")

    print()


def display_movies(movies, title_term):
    """
    Display formatted movie table.
    """
    print(f"MOVIES - {title_term}")

    # Column formatting
    print(f"{'ID':4}{'Name':38}{'Year':6}"
          f"{'Mins':6}{'Category':10}")
    print("-" * 63)

    for movie in movies:
        print(f"{movie.id:<4d}"
              f"{movie.name:38}"
              f"{movie.year:<6d}"
              f"{movie.minutes:<6d}"
              f"{movie.category.name:10}")

    print()


def get_int(prompt):
    """
    Safely obtain integer input from the user.

    Why this function exists:
    --------------------------
    - Prevents program crashes caused by invalid input.
    - Encapsulates validation logic in one reusable place.
    - Demonstrates defensive programming.

    Control Flow:
    -------------
    - Infinite loop continues until valid integer is entered.
    - ValueError is raised if conversion fails.
    - User is prompted again without terminating program.

    This improves:
    - Reliability
    - User experience
    - Code reuse
    """

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid whole number. Please try again.\n")


def display_movies_by_category():
    """
    Flow:
    1. Get category ID
    2. Validate category exists
    3. Retrieve movies
    4. Display results
    """
    category_id = get_int("Category ID: ")
    category = db.get_category(category_id)

    if category is None:
        print("There is no category with that ID.\n")
    else:
        print()
        movies = db.get_movies_by_category(category_id)
        display_movies(movies, category.name.upper())


def display_movies_by_year():
    """
    Retrieve and display movies by year.
    """
    year = get_int("Year: ")
    print()
    movies = db.get_movies_by_year(year)
    display_movies(movies, year)


def add_movie():
    """
    Add a new movie to the database.
    """
    name = input("Name: ")
    year = get_int("Year: ")
    minutes = get_int("Minutes: ")
    category_id = get_int("Category ID: ")

    category = db.get_category(category_id)

    if category is None:
        print("There is no category with that ID. Movie NOT added.\n")
    else:
        movie = Movie(
            name=name,
            year=year,
            minutes=minutes,
            category=category
        )

        db.add_movie(movie)
        print(f"{name} was added to database.\n")


def delete_movie():
    """
    Delete movie by ID.
    """
    movie_id = get_int("Movie ID: ")
    db.delete_movie(movie_id)
    print(f"Movie ID {movie_id} was deleted from database.\n")


def main():
    """
    Program entry point.
    Controls program flow.
    """
    db.connect()

    display_welcome()
    display_categories()

    while True:
        command = input("Command: ").lower()

        if command == "cat":
            display_movies_by_category()
        elif command == "year":
            display_movies_by_year()
        elif command == "add":
            add_movie()
        elif command == "del":
            delete_movie()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()

    db.close()
    print("Bye!")


# Python best practice:
# Only run main() if file is executed directly
if __name__ == "__main__":
    main()