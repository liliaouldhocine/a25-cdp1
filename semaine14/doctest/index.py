def my_split(string, char=' '):
    """
    Docstring for my_split
    
    :param string: Description
    :param char: Description

    >>> my_split('Je suis une chaine', ' ')
    ['Je', 'suis', 'une', 'chaine']

    >>> my_split('Je suis une chaine')
    ['Je', 'suis', 'une', 'chaine']

    >>> my_split('Je suis une chaine', '')
    ['Je suis une chaine']
    """
    res = []
    current_list = []
    for c in string:
        if(c != char):
            current_list.append(c)
        else: 
            res.append("".join(current_list))
            current_list = []
    res.append("".join(current_list))

    return res


# my_split("Je suis une chaine", ' ')
if __name__ == "__main__":
    import doctest
    doctest.testmod()
