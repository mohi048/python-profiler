# python-profiler

This is a simple python program to check the arguments passed to a function. In verbose mode you can check the total time taken by each function call

### USAGE

1. Copy the file logger.py to the local directory and import it on your python program. If its on same directory just import it
```
from logger import profile_it
```
2. Decorate the targent function
```
@profile_it(verbose=True)
```

3. You need to set the argument `Verbose` to either true or false

4. If decorator(argument) set to `@profile_it(verbose=True)` it would profile the function runtime , would create and updated the file `performance.txt`

5. If decorator(argument) set to `@profile_it(verbose=False)` it would log only the arguments passed to function , would create and update the file `variables.txt`

6. Execute the python program to call the target function to be profiled

7. Check the new files created as `variables.txt` and `performance.txt` located on the base directory of logger.py for the results of profile
