a=[[1,2],[3,4]]
b=[[1,2],[3,4]]
c=[[0,0],[0,0]]
for i in range(len(a)):
  for j in range(len(a[0])):
   
   for k in range(len(b)):
            c[i][j] += a[i][k] * b[k][j]


print(c)