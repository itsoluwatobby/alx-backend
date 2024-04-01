#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments
page and page_size. The function should return a tuple of size
two containing a start index and an end index
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return start and end indices for pagination.

    Args:
        page (int): Page number.
        page_size (int): Number of items per page.
    """
    return (page * page_size - page_size, page * page_size)
