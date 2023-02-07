def is_sorted(integers):
    """
    Checks if a possibly empty list of integers is sorted in non-decreasing order.
    :param integers: a list of integers or an empty list
    :precondition: the list is sorted in non-decreasing order, which means that each integer in the list is equal to
    or greater than the preceding integer
    :post condition: determines if the list is sorted in non-decreasing order
    :return: the function returns true if the list is sorted in non-decreasing order and False if not
    >>> is_sorted([1,2,3])
    True
    >>> is_sorted([3,1,2])
    False
    """
    return integers == sorted(integers)


def main():
    """
    Runs the program.
    """
    check_sorted = is_sorted([1, 2, 4, 5])


if __name__ == "__main__":
    main()