import math
import time

def isPrime1(n):
    start_time = time.perf_counter()
    for i in range(2,n):
        if n%i==0:
            return False
    end_time = time.perf_counter()
    time_taken = end_time - start_time
    return True, f'Runtime for Naive method : {time_taken:.6f}'

def isPrime2(n):
    start_time = time.perf_counter()
    x = int(math.pow(n,0.5))
    for i in range(2,x):
        if n%i==0:
            return False
    end_time = time.perf_counter()
    time_taken = end_time - start_time
    return True, f'Runtime for Optimized method : {time_taken:.6f}'

x = None
while True:
    x=input('Enter the number : ')
    try:
        x=int(x)
        break
    except:
        print('Please enter a number.')
        continue

a1,b1 = isPrime1(x)
a2,b2 = isPrime2(x)
print(f'Results for Naive method - Output : {a1}, Runtime : {b1:.6f}')
print(f'Results for optimized method - Output : {a2}, Runtime : {b2:.6f}')
