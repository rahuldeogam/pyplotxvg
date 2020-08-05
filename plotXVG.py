import numpy as np
import matplotlib.pyplot as plt
import sys



x, y = [], []
check = ["title", "xaxis", "yaxis",'s0']
pTitle = "title"
xLabel = "X"
yLabel = "Y"
pLegend = ""

file = sys.argv[1]

with open(file) as f:
    for line in f:
        cols = line.split()
        if cols[0] == '@':
            str = " "
            if check[0] in cols:
                index = cols.index(check[0])
                strTemp = cols[index+1:len(cols)]
                pTitle = str.join(strTemp)
            if check[1] in cols:
                index = cols.index(check[1])
                strTemp = cols[index+2:len(cols)]
                xLabel = str.join(strTemp)
            if check[2] in cols:
                index = cols.index(check[2])
                strTemp = cols[index+2:len(cols)]
                yLabel = str.join(strTemp)
            if check[3] in cols:
                index = cols.index(check[3])
                strTemp = cols[index+2:len(cols)]
                pLegend = str.join(strTemp)


        if len(cols) == 2:
            if cols[0] != "@TYPE":
                x.append(float(cols[0]))
                y.append(float(cols[1]))



fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title(pTitle)
ax1.set_xlabel(xLabel)
ax1.set_ylabel(yLabel)
ax1.plot(x,y, c='r', label=pLegend)
leg = ax1.legend()
plt.show()
