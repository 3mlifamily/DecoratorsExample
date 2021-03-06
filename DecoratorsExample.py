
import time

def decorator_func_logger(target_func):
 def wrapper_func(*args, **kwargs):
   print("Before calling", target_func.__name__)
   target_func(*args, **kwargs)
   print("After calling", target_func.__name__)
 
 return wrapper_func

def decorator_func_timeit(target_func):
    def wrapper_func(*args, **kwargs):
        ts = time.time()
        target_func(*args, **kwargs)
        te = time.time()
        print (target_func.__name__, (te - ts) * 1000)

    return wrapper_func

@decorator_func_logger
@decorator_func_timeit
def target(loop):
 count = 0
 print('Python is in the decorated target function')
 for number in range(loop):
    count += number

target(100)
target(3000)