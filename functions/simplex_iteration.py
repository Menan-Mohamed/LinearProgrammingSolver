import sys
import numpy as np


def simpleximplementation(tableau,vararr,basicarr,maxi):
    
    nparr = np.array(tableau, dtype=float)

    row, col = nparr.shape 

    flagend = 1

    while(flagend):

        if maxi :
            pivotcol = np.argmin(nparr[0][:-1])
        else :
            pivotcol = np.argmax(nparr[0][:-1])

        minpos = 1000
        minrate = sys.maxsize
        for i in range (1,row):
            if nparr[i][pivotcol] > 0 :
                if nparr[i][col-1] / nparr[i][pivotcol] < minrate :
                    minpos = i
                    minrate = nparr[i][col-1] / nparr[i][pivotcol]

        if(minpos == 1000):
            print("infeasible")
            break

        basicarr[minpos-1] = vararr[pivotcol]

        nparr[minpos] = nparr[minpos]/nparr[minpos][pivotcol]

        for i in range (row):
            if i == minpos : continue
            nparr[i] = -1*nparr[i][pivotcol]*nparr[minpos] + nparr[i] 

        flagend = 0
        if maxi :
            for i in range (col-1):
                if nparr[0][i] < 0 :
                    flagend = 1
        else: 
            for i in range (col-1):
                if nparr[0][i] > 0 :
                    flagend = 1

    print(vararr)
    print(basicarr)
    np.set_printoptions(suppress=True, precision=2)
    print(nparr)

    return nparr,vararr,basicarr




# var = ["x1","x2","x3","x4","s1","s2","s3"]
# basic = ["s1","s2","s3"]
# arr = [[-5,4,-6,8,0,0,0,0],
#        [1,2,2,4,1,0,0,40],
#        [2,-1,1,2,0,1,0,8],
#        [4,-2,1,-1,0,0,1,10]]
# maxi = 0
# simpleximplementation(arr,var,basic,maxi)