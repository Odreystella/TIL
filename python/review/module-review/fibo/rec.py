def get_fibo(num):
    if num < 2:
        return num
    else:
        return get_fibo(num-1) + get_fibo(num-2)
    
#print(get_fibo(5))
