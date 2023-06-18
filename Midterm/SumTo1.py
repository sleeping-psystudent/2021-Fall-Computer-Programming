def gcd(a,b):
    if b == 0:
        return a
    elif a < b:
        return gcd(b, a)
    else:
        return gcd(b, a % b)
    
def solution(X, Y):
    d = {}
    # dictionary
    for i in range(len(X)):
        fr = (X[i]/gcd(X[i], Y[i])),  (Y[i]/gcd(X[i], Y[i]))
        if fr in d:
            d[fr] += 1
        else:
            d[fr] = 1
    # print(d)    
    count = 0
    for index, values in enumerate(d):
        if (values[1]-values[0], values[1]) == (1.0, 2.0):
            count += d[(1.0, 2.0)]*(d[(1.0, 2.0)]-1)
        elif (values[1]-values[0], values[1]) in d:
            count += d[(values[0], values[1])]*d[(values[1]-values[0], values[1])]
    return int(count/2)
