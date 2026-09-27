import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time() 
        result = func(*args,**kwargs)
        end = time.time()
        timing = end - start
        print(f'the function {func.__name__} execution time is {timing:.4f}')
        return result
    return wrapper