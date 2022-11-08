def unique_in_order(iterable):
    line = []
    for i in iterable:
        if len(line) < 1 or not i == line[len(line) - 1]:
            line.append(i)
    return line
