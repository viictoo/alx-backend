#!/usr/bin/env python3
"""
function to return a tuple of size two containing a 
start index and an end index corresponding to the range of
indexes to return in a list for those particular pagination
parameters"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """_summary_

    Args:
        page (int): _description_
        page_size (int): _description_

    Returns:
        Tuple[int, int]: _description_
    """
    return ((page - 1) * page_size, page * page_size)