import random
def estimate_pi(n):
    num_point_circle=0;
    num_point_total=0;
    for i in range(n):
         x=random.uniform(0,1)
         y=random.uniform(0,1)
         distance=(x**2+y**2)
    if distance<1:
        num_point_circle+=1
        num_point_total+=1
    num_point_total=+1
    return 4*num_point_circle/num_point_total
print(estimate_pi(100))
import math
a=estimate_pi(10)
error=-100*((math.pi-estimate_pi(100))/math.pi)
print("My estimate of pi was {:.2f} so my error percentage to actual pi was {:.2f}.".format(a,error)) 
