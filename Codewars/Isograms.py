def is_isogram(string):
    string = string.upper()
    for i in range(len(string)):
        if string.count(string[i]) >= 2:
            return False
        else: continue
    return True
