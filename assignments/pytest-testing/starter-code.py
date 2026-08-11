"""Starter code for pytest testing assignment."""

from typing import List


def add_numbers(numbers: List[float]) -> float:
    """Return the sum of a list of numbers."""
    return sum(numbers)


def is_palindrome(text: str) -> bool:
    """Return True if the text is a palindrome, ignoring case and spaces."""
    normalized = ''.join(text.lower().split())
    return normalized == normalized[::-1]


def find_max(values: List[int]) -> int:
    """Return the maximum value from a non-empty list of integers."""
    if not values:
        raise ValueError("values must not be empty")
    return max(values)


if __name__ == "__main__":
    print("This file defines functions for pytest tests.")
