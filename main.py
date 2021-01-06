import string
import numpy as np


def get_eng_char(no_of_char):
    """
    Returns non-repeated randomly selected ASCII letters and digits.
    If no_of_char are greater than available English character set (i.e 62) function will
    return repeated randomly selected ASCII letters and digits.

    Args:
        no_of_char (int): Number of characters to return

    Returns:
        list: List of selected characters
    """
    # All ASCII letters and digits
    eng_char_set = list(string.ascii_letters + string.digits)

    # Randomly select characters
    if no_of_char <= len(eng_char_set):
        # replace=False is for non repeated selection.
        return np.random.choice(eng_char_set, no_of_char, replace=False)

    return np.random.choice(eng_char_set, no_of_char)


if __name__ == "__main__":

    # Get 55 random English charcters
    rand_eng_char = get_eng_char(55)
    print(rand_eng_char)

    # This list of characters can be passed further for eye chart display function accordingly

