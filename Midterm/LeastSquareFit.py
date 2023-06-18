def solution(A):
    sx = 0
    sy = 0
    for value in A:
        sx += value[0]
        sy += value[1]
    mx = sx/len(A)
    my = sy/len(A)

    Num = 0
    DenX = 0
    DenY = 0
    for value in A:
        Num += (value[0]-mx)*(value[1]-my)
        DenX += (value[0]-mx)**2
        DenY += (value[1]-my)**2
    if Num == 0.0:
        B1 = 0.0
    else:
        B1 = Num/(DenX*DenY)**(0.5)
    B0 = my-B1*mx
    return [B0, B1]

if __name__ == "__main__":
    q = [tuple([float(i) for i in j.split(',')]) for j in input().split('_')]
    print(tuple([round(i,5) for i in solution(q)]))

0,0_0,1_0,2_0,3
(1.5, 10000000000.0)
