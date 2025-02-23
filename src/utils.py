def square_list(numbers):
    """
    Returns a list with each number squared.
    
    :param numbers: List of integers
    :return: List of squared integers
    """
    return [num ** 2 for num in numbers]

def is_palindrome(text):
    """
    Checks if a given string is a palindrome.
    
    :param text: Input string
    :return: True if palindrome, False otherwise
    """
    return text == text[::-1]