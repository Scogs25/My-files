import matplotlib.pyplot as plt
import numpy as np
import math
import random
import pandas as pd 
random.seed(1)
def dice_roll_test(n):
    dice_options=range(0,7,1)
    res=[]
    for i in range(n):
        z=random.choice(dice_options)
        res.append(z)
        i+=1
    return res
print(dice_roll_test(n=20))
def dice_counter(n):
    b=dice_roll_test(n)
    counter={}
    for i in range(len(b)):
        if i <= 6:
            counter[i]=b.count(i)
        else:
            continue
    return counter
    
print(dice_counter(20))
plt.figure(1,figsize=(10,7))
plt.xlabel("Value of Dice Roll")
plt.ylabel("Frequency")
plt.title("Frequency of Dice Values in 100,000 Rolls")
plt.plot(dice_counter(100000).keys(),dice_counter(100000).values(),'b.',label='sample probabilties')
x_val=range(0,7,1)
actual_prob=100000/6
y_val_list=[actual_prob for i in x_val]
plt.plot(x_val,y_val_list,'r.',label="estimated probabilities")
plt.legend(loc='best')
plt.show()
plt.figure(2,figsize=(10,7))
error_list=[]
y_2=list((dice_counter(100000).values()))
for i in range(len(x_val)):
    error=((y_val_list[i]-y_2[i])/(y_val_list[i]))*100
    error_list.append(error)
plt.figure(2,figsize=(10,7))
plt.plot(x_val,error_list,'b.',)
plt.xlabel("value of dice roll")
plt.ylabel("Error of Sample Probability (%)")
plt.title("Error of Dice Roll Sample Probabilities (100,000 rolls)")
plt.show()
avg_error=sum(error_list)/len(error_list)
print(avg_error)
#from sklearn.linear_model import LinearRegression
#model = LinearRegression()
#model.fit(k, v)
#model = LinearRegression().fit(k, v)

