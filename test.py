# readlines.py
import numpy as np
f = open("basics.txt", 'r')
gwamok1 = []
for line in f:
    line = line.strip()
    list= line.split('	', 6)
    gwamok1.extend([list])
    gwamok = np.array(gwamok1)
print(gwamok)
f.close()
