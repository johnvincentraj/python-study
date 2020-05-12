def outer():
    x = 'old'    
    def changer():
        nonlocal x; 
        x = 'new'
    print('before run changer', x)
    changer()
    print('after run changer', x)
    
outer()
