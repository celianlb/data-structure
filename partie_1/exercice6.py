"""
    exercice 6
"""
n = [0,1]
m=10
def fib(n,m):
    i=1
   
    for i in range(i,m):
        resultat=n[i]+n[i-1]
        n.append(resultat)
    print(n)

fib(n,m)
