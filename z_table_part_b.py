import math
import matplotlib.pyplot as plt
import scipy.integrate 
import numpy as np
import statistics

def z_distribution(val):
    
    x = []
    y = []
    i = -4
    while i<=4:
        i+=0.01
        x.append(round(i,3))
    c = 1/(2*math.pi)**0.5

    for j in x:
        power = (-j ** 2) / 2
        dist = c * (math.e ** power)
        y.append(dist)
    #plt.plot(x,y)
    #plt.show()

    ninf = -float('inf')
    z=0


    def f(x):
        c = 1/(2*math.pi)**0.5
        power = (-x ** 2)/2
        std_norm_curve = c*(math.e ** power)
        return std_norm_curve

    probability, error = scipy.integrate.quad(f, ninf, z)
    print(round(probability, 4))

    z_table =[]
    for row in x:
        probability, error = scipy.integrate.quad(f, ninf, row)
        z_table.append([row, round(probability,4)])
        #print(row, round(probability,5))
        
        

    s = 0
    sos = 0
    for i in z_table:
        s += i[0]
    mean = s / len(z_table)    
    for i in z_table:
        temp = i[0] - mean
        sos += temp**2
    varience = sos / len(z_table)
    std = varience ** 0.5
    print (mean)
    print(std)
    
    for i in z_table:
        i[0] = (i[0] - mean)/std
        i[0] = round(i[0],2)
    
    for row in z_table:
        if abs(val-row[1]) < 0.001:
            z = row[0]
            print(f"z_value = {z}")
            break
    


def main():
    val = float(input('probability: '))
    val = round(val,4)
    z_distribution(val)
    
if __name__ == '__main__':
    main()
