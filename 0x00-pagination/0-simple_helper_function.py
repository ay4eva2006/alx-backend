#!/usr/bin/env python3
"""A function that find pagination"""


def index_range(page: int, page_size: int)  -> tuple:
    """returns index range for item"""
    return (((page-1)*page_size),page * page_size)
