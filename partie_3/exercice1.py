"""
exo1
"""

def hex(r,g,b):
    if 0<= r <=255 and 0<= g <=255 and 0<= b <=255 and type(r)==int and type(g)==int and type(b)==int:
        print(r)
        print(g)
        print(b)
        print('{:02X}{:02X}{:02X}'.format(r, g, b))

    
hex(255,0,0)
