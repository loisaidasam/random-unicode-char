random-unicode-char
===================

Python lib for generating a random unicode character, scraped from http://unicode.bloople.net

# Usage

    >>> from randomunicodechar import get_random_unicode_char
    >>> print get_random_unicode_char()
    (u'\ufffd', u'BYZANTINE MUSICAL SYMBOL KYLISMA (1D061)')
    >>> char, name = get_random_unicode_char()
    >>> print char, name
    ⌤ UP ARROWHEAD BETWEEN TWO HORIZONTAL BARS (2324)
