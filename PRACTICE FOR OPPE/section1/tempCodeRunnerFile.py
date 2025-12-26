def center_switch(t: tuple, val: int) -> tuple:
    # Your code here 
    l = len(t)
    mid = l//2
    if l%2 == 0:
        return t[:mid] + (val,) + t[mid:]
    else :
        return t[:mid] + (val,) + t[mid+1:]
print(center_switch((1, 2, 3),99))