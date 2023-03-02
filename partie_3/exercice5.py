"""
exo5
"""

def insert(lst):
    if isinstance(lst, list) or len(lst) == 30:
        for i in range(1, len(lst)):
            key = lst[i]
            j = i - 1
            while j >= 0 and lst[j] > key:
                lst[j+1] = lst[j]
                j -= 1
            lst[j+1] = key
        return lst
    else:
        return "liste de 30 entiers."
list=["Axel","axel","Axel","axel","Axel","axel","Axel","axel","Axel","axel","Axel","axel","Axel","axel","Axel","axel","Axel","axel","Axel","axel","Axel","axel","Axel","axel","Axel","axel","Axel","axel","Axel","axel"]

insert(list)