import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def derivative1(m, c, x, y):
    s = 0
    for i in range(len(x)):
        s += (c + m * x[i]) - y[i]
    return (1 / len(x)) * s

def derivative2(m, c, x, y):
    s = 0
    for i in range(len(x)):
        s += ((c + m * x[i]) - y[i]) * x[i]
    return (1 / len(x)) * s

def error_fun(m, c, x, y):
    return (1 / (2*len(x))) * sum(((c + m * x) -y) ** 2)
    
x = np.arange(30) 
y = 9 + 12 * x

m = 0
c = 0
learning_rate = 0.001

cost_m = np.linspace(0, 25, 100)
new_m = []

for i in cost_m:
    new_m.append(error_fun(m=i, c=0, x=x, y=y))

plt.plot(cost_m, new_m)

for i in range(1000):
    d1 = derivative1(m, c, x, y)
    d2 = derivative2(m, c, x, y)
    
    temp_c = c -  learning_rate * d1
    temp_m = m -  learning_rate * d2
    
    c = temp_c
    m = temp_m
    cost = error_fun(m=m, c=c, x=x, y=y)
    
    print('i = {}, m = {:.2f}, c = {:.2f}, cost = {:.2f}'.format(i, m, c, cost))
    plt.scatter(x=m, y=error_fun(m=m, c=c, x=x, y=y))
    plt.pause(0.0000001)    
plt.show()
