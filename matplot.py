import matplotlib.pyplot as plt
import numpy as np
import math
x=np.arange(0, math.pi*2, 0.05)
y=np.sin(x)
plt.plot(x,y)
plt.xlabel("\u03F4")
plt.ylabel("Sin(\u03F4)")
plt.title("Sine Wave")
plt.figure(1)
plt.show()
def savings_calc(init_bal,sav_per,des_bal):
    balance=0
    year=1
    bal_list=[init_bal]
    while balance<des_bal:
        balance+=init_bal*(1+sav_per)**year
        bal_list.append(balance)
        year+=1
    return bal_list
Y=list(savings_calc(2000,.05,10000))
X=range(0,6,1)
plt.plot(X,Y,'r.')
plt.figure(2)
plt.show()
import random
dice_options=range(0,7,1)
z=random.choice(dice_options)
print(z,dice_options)
