# by useing for loop
import time
def selectionsort(a):
    n=len(a)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if(a[j]<a[min]):
                min=j
        temp=a[i]
        a[i]=a[min]
        a[min]=temp
start=time.time()
a=[34,46,43,27,57,41,45,21,70]
selectionsort(a)
print(a)
end=time.time()
print("Runtime of the programme is",end-start)