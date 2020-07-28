class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
my_vector=Vector([1,2])
my_vector_2=Vector([2,3])
import math
test_vec=[3,4,5]
def add_vec(a,b):
    Result=[x+y for x,y in zip(a,b)]
    return Result
def minus_vec(a,b):
    Result=[x-y for x,y in zip(a,b)]
    return Result
def scal(a,c):
    b=[x*c for x in a]
    return b
def vect_mag(a):
    sum=0
    for i in range(len(a)):
        sum+=(a[i])**2
    return math.sqrt(sum)
print(vect_mag(test_vec))
def vect_norm(a):
    res=(vect_mag(a))**-1
    return scal(a,res)
vec_1=[-0.221,7.437]
vec_2=[8.813,-1.331,-6.247]
vec_3=[5.581,-2.136]
vec_4=[1.996,3.108,-4.554]
print("Question one answer is {:.3f} and Question two answer is {:.3f}".format(vect_mag(vec_1),vect_mag(vec_2)))
print(vect_norm(vec_3),vect_norm(vec_4))
from functools import reduce
def dot_prod(a,b):
    list_1=[x*y for x,y in zip(a,b)]
    return sum(list_1)
v_1=[7.887,4.138]
v_2=[-5.955,-4.904,-1.874]
w_1=[-8.802,6.776]
w_2=[-4.496,-8.755,7.103]
print("Q1 Answer:{:.3f}".format(dot_prod(v_1,w_1)))
print("Q2 Answer:{:.3f}".format(dot_prod(v_2,w_2)))
#dot prod would default ouput in rads so included conversion to degrees
def dot_angle(a,b):
    res=(dot_prod(a,b))/(vect_mag(a)*vect_mag(b))
    return (math.acos(res))*(180/math.pi)
v_3=[3.183,-7.627]
v_4=[7.35,0.221,5.188]
w_3=[-2.668,5.319]
w_4=[2.751,8.259,3.985]
print("Q3 answer {:.3f}".format(dot_angle(v_3,w_3)*(math.pi/180)))
print("Q4 answer {:.3f}".format(dot_angle(v_4,w_4)))
def orth(a,b):
    if dot_prod(a,b)==0:
        return "orthogonal!"
    return "Not othogonal"
def parallel(a,b):
    for c in range(-100,100):
        if scal(a,c) == b:
            return "Parallel"
    return "not Parallel"
v_5=[-7.579,-7.88]
v_6=[-2.029,9.97,4.172]
v_7=[-2.328,-7.284,-1.214]
v_8=[2.118,4.827]
w_5=[22.737,23.64]
w_6=[-9.231,-6.639,-7.245]
w_7=[-1.821,1.072,-2.94]
w_8=[0,0]
print(parallel(v_5,w_5),orth(v_5,w_5))
print(parallel(v_6,w_6),orth(v_6,w_6))
print(parallel(v_7,w_7),orth(v_7,w_7))
print(parallel(v_8,w_8),orth(v_8,w_8))
#projection functions 
def project_vec(a,b):
    res=(dot_prod(a,b))/(vect_mag(b)**2)
    return scal(b,res)
def project_vec_perp(a,b):
    perp=minus_vec(a,project_vec(a,b))
    return perp
proj_v=[3.039,1.879]
proj_b=[.825,2.036]
proj_v_1=[-9.88,-3.264,-8.159]
proj_b_1=[-2.155,-9.353,-9.473]
proj_v_2=[3.009,-6.172,3.692,-2.51]
proj_b_2=[6.404,-9.144,2.759,8.718]
q1_ans=project_vec(proj_v,proj_b)
q2_ans=project_vec_perp(proj_v_1,proj_b_1)
q3_ans=(project_vec(proj_v_2,proj_b_2),project_vec_perp(proj_v_2,proj_b_2))
print(q1_ans,q2_ans,q3_ans)
#cross product,paralleogram, and triangle funcs 
def cross_prod(a,b):
    cross_list=[]
    x=(a[1]*b[2])-(b[1]*a[2])
    cross_list.append(x)
    y=-1*((a[0]*b[2])-(b[0]*a[2]))
    cross_list.append(y)
    z=(a[0]*b[1])-(b[0]*a[1])
    cross_list.append(z)
    return cross_list
print(cross_prod([8.462,7.893,-8.187],[6.984,-5.975,4.778]))
def parallelogram_area(a,b):
    return vect_mag(cross_prod(a,b))
print(parallelogram_area([-8.987,-9.838,5.031],[-4.268,-1.861,-8.866]))
def triangle_area(a,b):
    return 0.5*parallelogram_area(a,b)
print(triangle_area([1.5,9.547,3.691],[-6.007,0.124,5.772]))
import numpy 
def line_parallel(a,b):
    for i in numpy.arange(-100,100,.25):
        if scal(a,i)[:2]==b[:2]:
            return "Parallel"
        elif scal(a,i)==b:
            return "Parallel Same line"
        else:
            return "not Parallel not  same line"
print(line_parallel([4.046,2.836,1.21],[10.115,7.09,3.025]))
print(line_parallel([7.204,3.182,8.68],[8.172,4.114,9.883]))
print(line_parallel([1.182,5.562,6.744],[1.773,8.343,9.525]))
def line_intersec(a,b):
    x=((b[1]*a[2])-(a[1]*b[2]))/((a[0]*b[1])-a[1]*b[0])
    y=((-b[0]*a[2])+a[0]*b[2])/((a[0]*b[1])-a[1]*b[0])
    res=[x,y]
    if len(res)==2:
        return res
    elif len(res)<2:
        return "Parallel Lines, No intersection"
    elif len(res)>2:
        return "Same Line,Infinite solutions"
print(line_intersec([7.204,3.182,8.68],[8.172,4.114,9.883]))
def plane_parallel(a,b):
    for i in range(len(a)-1):
        if b[i]/a[i] == b[i+1] / a[i+1]:
            return "Parallel"
        else:
            return "Not Parallel"
print(plane_parallel([-7.926,8.625,-7.217],[-2.642,2.875,-2.404]))