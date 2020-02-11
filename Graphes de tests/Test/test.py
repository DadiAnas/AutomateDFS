d={}
d[(0,0)]=10
d[(0,1)]=5

def verify(i,j,x,d):
    try:
        if(d[(i, j)]):
            d[(i, j)]=x
    except KeyError:
        print("({},{}) is not a key".format(i,j))

verify(0,3,2,d)
verify(0,0,2,d)
print(d)