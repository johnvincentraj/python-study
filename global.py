x = 'old'
def changer():
    global x;
    x = 'new'

print('x value before global :', x)
changer()
print('x value after global :, ', x)
print(x)
