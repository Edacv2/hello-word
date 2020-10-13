def fibonacci(number, fib_series):
    """This function will calculate the Fibinacci, it use number(terminating conditions) and a serie[] (to start) as an arguments"""
    if number < 2 :
        return
    l = len(fib_series)
    
    new_number = fib_series[l -1] + fib_series[l - 2]
    
    fib_series.append(new_number)
    
    print("Series so far", fib_series) #Validation
    
    fibonacci(number - 1, fib_series)

print(fibonacci(5,[0,1]))
# This fuction is a great example for Python recusion, to better understan is advise to debug and see what the invocator and the calles have.