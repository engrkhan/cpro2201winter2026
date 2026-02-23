"""
objects.py

This module defines the domain (business) objects used in the program.
We use dataclasses to reduce boilerplate code.
"""

# dataclass automatically generates:
# - __init__()
# - __repr__()
# - __eq__()
# and other useful methods
from dataclasses import dataclass


@dataclass
class Category:
    """
    Represents a movie category (e.g., Action, Drama, Comedy).

    This class maps directly to a row in the Category table
    in the database.
    """
    id: int = 0        # Primary key in database
    name: str = ""     # Category name


@dataclass
class Movie:
    """
    Domain Model representing a Movie entity.

    This class corresponds to the Movie table in the database.
    
    Architectural Insight:
    -----------------------
    - 'category' is not stored as a simple integer ID.
      Instead, it is stored as a Category object.
    - This demonstrates object composition.
    - This design improves readability and reduces coupling
      between database logic and UI logic.

    Example:
    --------
    movie.category.name   # Direct access without extra lookup
    """
    id: int = 0
    name: str = ""
    year: int = 0
    minutes: int = 0
    category: Category = None   # Relationship to Category object