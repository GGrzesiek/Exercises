def reverse(text):
    """Reverse a string."""
    tabtext = list(text)
    tabtext.reverse()
    revtext = "".join(tabtext)
    return revtext