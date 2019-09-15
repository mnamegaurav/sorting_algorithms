#Quick Sort algorithm

def quick_sort(l,start,end):
    pivot = end
    i,j=start,start
    
    if end-start<=1:
        return
    
    while j<=pivot:
        if j==pivot:
            l[j],l[i]=l[i],l[j]
            break
        elif l[j]>=l[pivot]:
            j+=1
        elif l[j]<l[pivot]:
            l[j],l[i]=l[i],l[j]
            i+=1
            j+=1
   
    quick_sort(l,start,i-1)
    quick_sort(l,i+1,end)
    
    return l    