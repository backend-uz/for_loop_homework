def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    list1 = []
    r = range(n)
    for i in r:
        list1.append(k)
    return list1
print(main(5,3))