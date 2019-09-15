#Selection Sort algorithm

def selection_sort(l):
    for i in range(0,len(l)-1):
        min_pos = i
        for j in range(i+1,len(l)):
            if l[min_pos] > l[j]:
                min_pos = j
        if min_pos != i: #this is extra line for  me
            (l[i],l[min_pos]) = (l[min_pos],l[i])
    return l            