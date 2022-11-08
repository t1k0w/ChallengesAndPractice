def to_jaden_case(string):
    s = string.split(" ")
    result = ''
    for i in s: 
        print(i)
        result = result + i[0].upper() + i[1 : len(i)].lower() + " "
    return result.rstrip()
