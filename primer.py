
def print_words(word, counts):
    """
    IN: word, a string and counts, an int
    OUT: A string that is word repeated int many times

    >>> print_words(5, 7)
    Hey, I wanted a string
    >>> print_words('Loftus', 7)
    LoftusLoftusLoftusLoftusLoftusLoftusLoftus
    >>> print_words('Loftus', 7.0)
    Hey, I want an integer
    """
    
    if isinstance(word, str) and isinstance(counts, int):
        print word*counts
    elif not isinstance(word, str):
        print word*counts
    elif not isinstance(counts, int):
        print 'Hey, I want an integer'
    else:
        print "hey, I want a string and an int"

#################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
