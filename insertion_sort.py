#Insertion Sort algorithm

def insertion_sort(l):
    for i in range(1,len(l)):
        curr_num = l[i]
        while curr_num < l[i-1] and i-1>=0:
            l[i-1], l[i] = l[i],l[i-1]
            i-=1
    return l