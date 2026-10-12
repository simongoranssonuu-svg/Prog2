""" MA3.py

Student: Simon Göransson
Mail: SimonRaf04@hotmail.se
Reviewed by:
Date reviewed:

"""
import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc
from matplotlib.patches import Rectangle, Circle

from numba import njit


# Exc1
def approximate_pi(n):

    xIn = []
    yIn = []
    xOut = []
    yOut = []

    inCircle = 0

    for dot in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 < 1:
            xIn.append(x)
            yIn.append(y)
            inCircle += 1
        else:
            xOut.append(x)
            yOut.append(y)

    plt.plot(xIn, yIn, '.', color='red')
    plt.plot(xOut, yOut, '.', color='blue')

    plt.show()

    print(f"Number of points n is: {n}")
    print(f"The approximation of pi for this amount of points is: {4*inCircle/n}")
    
    return

# Exc2, approximation
def sphere_volume(n, d): 

    result = list(filter(lambda x: x < 1, [sum(map(lambda x: x**2, [random.uniform(-1,1) for dim in range(d)])) for dots in range(n)]))

    # [random.random() for dim in range(d)]
    #[sum(map(lambda x: x**2, 
    #  for dots in range(n)
    #filter(lambda x: x < 1,
    
    return (2**d *len(result)/n)
    # antar att när radien är 1 blir volymen bara denna kvot
    

#Exc2, real value
def hypersphere_exact(n, d):
    return (m.pi**(d/2))/m.gamma((d/2)+1)

#Exc3: numba version
@njit
def sphere_volume_numba(n:int, d:int)->float:
    count = 0
    for dots in range(n):
        sum = 0
        for dim in range(d):
            sum += random.uniform(-1,1)**2

        if sum < 1:
            count +=1
    
    #np is the number of processes
    return (2**d *count/n)

#Exc4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n, d, np=10):
    start = pc()

    with future.ProcessPoolExecutor() as ex:
        results = []

        for process in range(np):
            result = ex.submit(sphere_volume, n//np, d)
            results.append(result)

        finalResults = [r.result() for r in results]

    return 
    
def main():
    '''# Exc1
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)'''

    '''# Exc2
    n = 100000
    d = 2
    print(sphere_volume(n, d))
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

    n = 100000
    d = 11
    print(sphere_volume(n, d))
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")
'''
    # Exc3
    '''n = 1000000
    d = 11

    for i in range(3):
        start = pc()
        sphere_volume(n, d)
        stop = pc()

        print(f"Call {i+1} without numba took {stop - start} seconds")

    for i in range(3):
        start = pc()
        sphere_volume_numba(n, d)
        stop = pc()

        print(f"Call {i+1} with numba took {stop - start} seconds")'''

     # Exc4
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n, d)
    stop = pc()
    print(f"Exc4: Sequential time of {d} and {n}: {stop-start}")

    start = pc()
    sphere_volume_parallel2(n, d)
    stop = pc()
    print(f"Exc4: Sequential time of {d} and {n} with parallel: {stop-start}")


    
    

if __name__ == '__main__':
	main()
