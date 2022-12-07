def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    x = str(list(range(n)))
    j = ','.join(x)
    return x
print(main(3))