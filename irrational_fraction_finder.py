import math

num_1 = float(input("Enter any irrational number :- "))
num_2 = int(input("Enter max number to be used in denominator :- "))
num_3 = int(input("Enter min number to be used in denominator :- "))

int_part = int(num_1)

d = {}
for j in range(num_3,num_2):
    for i in range(int(j*num_1),num_2*int_part):
        if math.gcd(i, j) != 1:
            continue
        if i/j > num_1:
            d[abs(i/j - num_1)] = [i,j,i/j,abs(i/j - num_1)]
            break
        elif i//j == int_part:
            d[abs(i/j - num_1)] = [i,j,i/j,abs(i/j - num_1)]
print(d[min(d)])
