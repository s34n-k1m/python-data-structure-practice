def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    letters = list(phrase)
    newWord = ""

    for letter in letters:
        if letter == to_swap:
            newWord += letter.swapcase()
        elif letter.swapcase() == to_swap:
            newWord += letter.swapcase()
        else:
            newWord += letter
    
    return newWord


