"""
db.py

This module handles ALL interaction with the SQLite database.

Key Concept:
-------------
This is called a Data Access Layer (DAL).
It isolates database logic from the user interface.
"""

import sqlite3
from contextlib import closing
from pathlib import Path

from objects import Category, Movie

# Global connection variable
# Only one connection is maintained during program execution
conn = None


def connect():
    """
    Establish a connection to the SQLite database.

    Why global?
    Because multiple functions need access to the same connection.
    """
    global conn

    if not conn:  # Prevent multiple connections
        DB_FILE = Path(__file__).parent / "movies.sqlite"

        # Connect to database file
        conn = sqlite3.connect(DB_FILE)

        # This allows us to access columns by name instead of index
        # row["movieID"] instead of row[0]
        conn.row_factory = sqlite3.Row


def close():
    """
    Close database connection safely.
    """
    if conn:
        conn.close()


# -------------------------------
# Object Mapping Functions
# -------------------------------

def make_category(row):
    """
    Convert a database row into a Category object.
    This is called Object-Relational Mapping (ORM).
    """
    return Category(row["categoryID"], row["categoryName"])


def make_movie(row):
    """
    Convert a database row into a Movie object.

    Notice:
    We also construct a Category object from the same row.
    """
    return Movie(
        row["movieID"],
        row["name"],
        row["year"],
        row["minutes"],
        make_category(row)
    )


def make_movie_list(results):
    """
    Convert a list of database rows into a list of Movie objects.
    """
    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies


# -------------------------------
# SELECT Queries
# -------------------------------

def get_categories():
    """
    Retrieve all categories from the database.
    """
    query = """
        SELECT categoryID, name as categoryName
        FROM Category
    """

    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    categories = []
    for row in results:
        categories.append(make_category(row))

    return categories


def get_category(category_id):
    """
    Retrieve a single category by its primary key.

    Parameters
    ----------
    category_id : int
        The ID of the category to retrieve.

    Returns
    -------
    Category | None
        - A Category object if found
        - None if no matching record exists

    Design Notes
    ------------
    - Uses parameterized query (?) to prevent SQL injection.
    - Uses context manager (with closing(...)) to ensure
      cursor resources are properly released.
    - This function is part of the Data Access Layer (DAL),
      isolating SQL logic from UI logic.
    """

    query = """
        SELECT categoryID, name AS categoryName
        FROM Category
        WHERE categoryID = ?
    """

    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        row = c.fetchone()

        return make_category(row) if row else None

def get_movies_by_category(category_id):
    """
    Retrieve all movies in a specific category.

    Demonstrates JOIN between Movie and Category tables.
    """
    query = """
        SELECT movieID, Movie.name, year, minutes,
               Movie.categoryID,
               Category.name as categoryName
        FROM Movie
        JOIN Category
            ON Movie.categoryID = Category.categoryID
        WHERE Movie.categoryID = ?
    """

    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        results = c.fetchall()

    return make_movie_list(results)


def get_movies_by_year(year):
    """
    Retrieve movies released in a specific year.
    """
    query = """
        SELECT movieID, Movie.name, year, minutes,
               Movie.categoryID,
               Category.name as categoryName
        FROM Movie
        JOIN Category
            ON Movie.categoryID = Category.categoryID
        WHERE year = ?
    """

    with closing(conn.cursor()) as c:
        c.execute(query, (year,))
        results = c.fetchall()

    return make_movie_list(results)


# -------------------------------
# INSERT / DELETE
# -------------------------------

def add_movie(movie):
    """
    Insert a new movie into the database.
    """
    sql = """
        INSERT INTO Movie (categoryID, name, year, minutes)
        VALUES (?, ?, ?, ?)
    """

    with closing(conn.cursor()) as c:
        c.execute(sql, (
            movie.category.id,
            movie.name,
            movie.year,
            movie.minutes
        ))

        # Required to permanently save changes
        conn.commit()


def delete_movie(movie_id):
    """
    Delete a movie by ID.
    """
    sql = "DELETE FROM Movie WHERE movieID = ?"

    with closing(conn.cursor()) as c:
        c.execute(sql, (movie_id,))
        conn.commit()