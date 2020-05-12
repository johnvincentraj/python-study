def sq(x):
    for i in range(x):
        yield i ** 2
    
a = sq(4)    

iter(a)
print(next(a))
print(next(a))
print(next(a))
