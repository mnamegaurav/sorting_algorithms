#Merge Sort algorithm

def merge(left_half,right_half):
    left_i = right_i = 0
    new_l = []
    while left_i < len(left_half) and right_i < len(right_half):
        
        if left_half[left_i] < right_half[right_i]:
            new_l.append(left_half[left_i])
            left_i += 1
            
        else:
            new_l.append(right_half[right_i])
            right_i += 1
            
    new_l.extend(left_half[left_i:])
    new_l.extend(right_half[right_i:])
    return new_l
    
def merge_sort(l):
    if len(l) <= 1:
        return l
    mid = len(l)//2
    left_half = merge_sort(l[:mid])
    right_half = merge_sort(l[mid:])   
    return merge(left_half,right_half)