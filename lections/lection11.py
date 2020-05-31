a = [2,3,5,4]
b = [1,2,3,4]

def lcs(a,b):
    f = [[0]*(len(b)+1) for i in range(len(a)+1)]
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1]==b[j-1]:
                f[i][j] = 1 + f[i-1][j-1]
            else:
                f[i][j] = max(f[i-1][j],f[i][j-1])
    return f

lcs(a,b)