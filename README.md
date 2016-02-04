# python-profiler

This is a simple python program to check the arguments passed to a function. In verbose mode you can check the total time taken by each function call

### USAGE

- Copy the file `logger.py` to the local directory and import it on your python program. If its on same directory just import it
```
from logger import profile_it
```
- Decorate the targent function
```
@profile_it(verbose=True)
```
- You need to set the argument `Verbose` to either true or false

- If decorator(argument) set to `@profile_it(verbose=True)` it would profile the function runtime , would create and updated the file `performance.txt`

- If decorator(argument) set to `@profile_it(verbose=False)` it would log only the arguments passed to function , would create and update the file `variables.txt`

- Execute the python program to call the target function to be profiled

- Check the new files created as `variables.txt` and `performance.txt` located on the base directory of logger.py for the results of profile
