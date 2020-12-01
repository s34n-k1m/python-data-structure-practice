def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    # there's a python built-in cap first letter
    return phrase[0].upper() + phrase[1:]

