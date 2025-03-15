import numpy as np

def simplex(arr, varnum, constraints):

    nparr = np.array(arr, dtype=float)
    maxi = nparr[0][varnum]
    
    vararr = np.array([f"x{i+1}" for i in range(varnum)] + [f"s{i+1}" for i in range(constraints)])
    basicarr = np.array([f"s{i+1}" for i in range(constraints)])

    nparr = np.delete(nparr, -2, axis=1)        #delete flags

    for i in range (constraints):
       nparr = np.insert(nparr, varnum, 0, axis=1)         #insert slags var

    j=0
    for i in range (1,constraints+1):               #edit the coeff
        nparr[i][varnum+j] = 1
        j += 1
    
    for i in range(varnum):
        nparr[0][i] *= -1

    flagend = 1

    while(flagend):
        if maxi :
            col = np.argmin(nparr[0])
        else :
            col = np.argmax(nparr[0])

        minpos = 1000
        minrate = nparr[1][varnum+constraints]
        for i in range (1,constraints+1):
            if nparr[i][col] > 0 :
                if nparr[i][varnum+constraints] / nparr[i][col] < minrate :
                    minpos = i
                    minrate = nparr[i][varnum+constraints] / nparr[i][col]

        if(minpos == 1000):
            print("infeasible")
            break

        basicarr[minpos-1] = vararr[col]

        nparr[minpos] = nparr[minpos]/nparr[minpos][col]

        for i in range (constraints+1):
            if i == minpos : continue
            nparr[i] = -1*nparr[i][col]*nparr[minpos] + nparr[i] 

        flagend = 0
        if maxi :
            for i in range (varnum+constraints):
                if nparr[0][i] < 0 :
                    flagend = 1
        else: 
            for i in range (varnum+constraints):
                if nparr[0][i] > 0 :
                    flagend = 1

    print(basicarr)
    print(nparr)


    



array = [[5,-4,6,-8,0,0],
         [1,2,2,4,-1,40],
         [2,-1,1,2,-1,8],
         [4,-2,1,-1,-1,10]]

simplex(array,4,3)