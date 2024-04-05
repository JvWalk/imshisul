import numpy as np

def all(Gwamok):
    f = open("basics.txt", 'w')
    for i in range(Gwamok.shape[0]):
        for j in range(Gwamok.shape[1]):
            f.write(Gwamok[i,j])
            f.write('\t') 
        f.write('\n')
    f.close()

