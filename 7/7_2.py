def recv(maxsize, *, block):
    'Receives a message'
    pass
# recv(1024, True) # TypeError
recv(1024, block=True) # Ok
recv(1024, block=False) # Ok



def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

mininum(1, 5, 2, -5, 10) # Returns -5
mininum(1, 5, 2, -5, 10, clip=0) # Returns 0

help(recv)