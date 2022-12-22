def comp(a, b):
    if a is None or b is None:
        return False
    
    if len(a) != len(b):
        return False

    b_sorted = sorted(b)
    
    for x in a:
        if x ** 2 not in b_sorted:
            return False
        b_sorted.remove(x ** 2)
    return True
                
