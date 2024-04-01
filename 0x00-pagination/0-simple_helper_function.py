#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments
page and page_size. The function should return a tuple of size
two containing a start index and an end index
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Return start and end indices for pagination.

    Args:
        page (int): Page number.
        page_size (int): Number of items per page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
