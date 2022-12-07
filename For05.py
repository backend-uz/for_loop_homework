def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """ 
    r = list(range(B,A-1,-1))
    return r
print(main(3,9))