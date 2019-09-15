#Bubble Sort algorithm

def bubble_sort(l):
    for j in range(0,len(l)):
        for i in range(0,len(l)-1):
            if l[i] > l[i+1]:
                l[i],l[i+1] = l[i+1],l[i]       
    return l