def bubble_sort(v,n):
    exibe(v,n)
    i = n
    while i > 1:
        empurra(v,i)
        exibe(v,i)
        i -= 1
    exibe(v,n)
    return

def empurra(v,n):
    i = 0
    while i < n-1:
        if v[i] > v[i+1]:
            troca(v,i,i+1)
        i += 1 #alt
    return

def troca(v,i,j):
    temp = v[i]
    v[i] = v[j]
    v[j] = temp
    return

def exibe(v,n):
    i = 0
    while i < n:
        print(v[i], end=' ')
        i += 1
    print('\n')
    return
