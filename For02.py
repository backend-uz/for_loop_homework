def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    x = (list(range(n)))
    i = 0
    list1 = []
    while i < len(x):
        list1.append(str(x[i]))
        i += 1
    j = ','.join(list1)
    return j
print(main(3))