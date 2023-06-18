def solution(X, Y):
    if X == 0 and Y == 0:
        return 0
    y = max(abs(X),abs(Y))
    x = -(y-1)
    count = (y*2-1)**2
    while x != X or y != Y:
        if -y+1 <= x and x < y and y > 0:
            x += 1
            count += 1
        elif y <= x and -y < x and x > 0:
            y -= 1
            count += 1
        elif x <= -y and y < x and y < 0:
            x -= 1
            count += 1
        elif y >= x and y < -x+1 and x <= 0:
            y += 1
            count += 1
            
    return count  
