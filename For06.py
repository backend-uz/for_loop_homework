def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    r = list(range(A,B+1))
    i = 0
    s = 0
    for i in r:
        s = s+i
    return s
print(main(1,5))