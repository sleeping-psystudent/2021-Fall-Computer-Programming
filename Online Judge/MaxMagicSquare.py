def solution(A):
    column = len(A)
    row = max(len(A[0]),len(A[len(A)-1]))
    
    for rows in A:
        if len(rows)!=row:
            rows.append(0)

    for i in range(min(column, row), 0, -1): # Column或Row比較小的
        for j in range(column-i+1): # 上下
            for m in range(row-i+1): # 左右
                # 對角線
                # print([A[j+c][m+c] for c in range(i)], [A[j+c][m+i-c-1] for c in range(i)])
                if sum([A[j+c][m+c] for c in range(i)])==sum([A[j+c][m+i-c-1] for c in range(i)]):
                    diagonal = sum([A[j+c][m+c] for c in range(i)])
                    # 橫線和直線
                    if sum(A[j][m:m+i])==sum([row[m] for row in A[j:j+i]]):
                        if (sum(A[j][m:m+i])==diagonal):
                            return i
    pass

"""
solution([[5,1,3,1],[9,3,3,1],[1,3,3,8]])
2
"""
