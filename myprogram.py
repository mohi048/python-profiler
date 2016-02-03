from logger import profile_me

@profile_me(verbose=True)
def gen(t):
    print t*t

@profile_me(verbose=True)
def generate(x):
    t = [i for i in xrange(x)]
    for items in t:
	gen(items)

generate(4)
