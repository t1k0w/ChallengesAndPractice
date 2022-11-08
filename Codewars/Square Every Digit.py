def square_digits(num):
    sum= str(num)
    answer = "" 
    for i in sum:
        answer += str(int(i) ** 2)
    return int(answer)
