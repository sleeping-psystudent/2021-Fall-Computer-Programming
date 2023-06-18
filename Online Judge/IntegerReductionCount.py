def solution(S):
    count = 0
    num = int(str(S),2)
 
    while num != 0:
        if num % 2 == 0:
            num = num/2
            count += 1
        else:
            num -= 1
            count += 1

    return count
    pass
