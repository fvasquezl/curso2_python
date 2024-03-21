def increment (x):
    return x+1

def high_order_function(x,func):
    return x+func(x)

result = high_order_function(2, increment)

print(result)


"""
----------------------------
"""
increment_v2= lambda x : x+1

high_order_function_v2 = lambda x,func: x+func(x)

result_v2 = high_order_function_v2(2, increment_v2)

print(result_v2)
