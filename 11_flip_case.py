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
    #making a new string at each iteration, so not very good run time
    newWord = ""

    for letter in letters:
        if letter.lower() == to_swap.lower():
            newWord += letter.swapcase()
        else:
            newWord += letter
    
    return newWord

    #improves run time and readibility
    #build up string, list than turn into string in the end is often much better performance

    letters = [letter.swapcase() if letter.lower() == to_swap.lower() else letter]

    return ''.join(letters)



