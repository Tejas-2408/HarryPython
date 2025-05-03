def fibbo(n):
    if n<=1:
        return n 
    return fibbo(n-2) + fibbo(n-1)

print(fibbo(5))