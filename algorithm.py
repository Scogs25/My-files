#peak finder algorithm
#1D case solution
def peak_finder(a):
    n=len(a)
    if a[int(n/2)]< a[int((n/2)-1)]:
        for i in range(int((n/2)-1),0,-1):
            if a[i]>a[i-1]:
                return "peak found. It's {}. The max peak of the array is {}.".format(a[i],max(a))
    elif a[int(n/2)]>a[int((n/2)-1)]:
        for i in range(int((n/2)),n,1):
            if a[i]>a[i+1]:
                return "peak found.It's {}.The max peak of the array is {}.".format(a[i],max(a))
    else:
        return "Peak found. It's {}.".format(a[n/2])
a=[1,2,5,9,4,3]
b=[100,50,75,65,80,70]
print(peak_finder(a))
print(peak_finder(b))

