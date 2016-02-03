## Author - Mohit. ((  Git -: http://github.com/mohi048  ))
## Python script to profile function arguments and performance

import cProfile
import time

def profile_me(verbose):
    def profile_it(func):
        def wrapper(*args, **kwargs):
            fh = open('variables.txt', 'a')
            fh.write('\n'+(time.strftime("[%d-%m-%Y %H:%M:%S]  ")) +\
            'Logging variables for function : ')
            fh.write(func.__name__+" : "+str(args)+" : "+str(kwargs))
            fh.close()
            if verbose:
                profile = cProfile.Profile()
                try:
                    profile.enable()
                    res = func(*args, **kwargs)
                    profile.disable()
                    return res
                finally:
                    tt = profile.getstats()
                    fh = open('performance.txt', 'a')
                    fh.write("\n"+(time.strftime("[%d-%m-%Y %H:%M:%S]  "))+\
                        "Profiling the function "+func.__name__+" on passing the variables "+" : "+str(args)+" : "+str(kwargs))
                    for items in tt:
                        code = items.code
                        callcount = items.callcount
                        recallcount= items.reccallcount
                        inlinetime = items.inlinetime
                        totaltime = items.totaltime
                        calls = items.calls
                        string = "\n\tCode : "+str(code) +\
                        "\n\tCall Count : "+str(callcount) +\
                        "\n\tRecursive Call : "+str(recallcount) +\
                        "\n\tTotal Time : "+str(totaltime) +\
                        "\n\tInline Time : "+str(inlinetime) +\
                        "\n\tCalls : "+str(calls) + "\n"
                        fh.write(string)
                        fh.close
            else:
                func(*args,**kwargs)
        return wrapper
    return profile_it

'''
@profile_me(verbose=True)
def print_me(x,y,z):
    print x
    print y
    print z

print_me(3,4,5)
print_me(1,2,3)
'''