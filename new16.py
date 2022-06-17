x='*'

for i in range(4,-1,-6):
    
    print(i*x)
    for j in range(2,-i,-6):

        print(j*x)
        for k in range(6,-i,-6):
            print(k*x)
            for l in range(3,-j,-6):
                print(l*x)
                for m in range(1,-l,-6):
                    print(m*x)
                    for n in range(4,-m,-6):
                         print(n*x)

