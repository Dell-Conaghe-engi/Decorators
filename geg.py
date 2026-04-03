from repeat import repeat_decorator

@repeat_decorator(times=2)
def pereborg():
    nums = range(1, 5)
    for i in nums:
        i = i ** 2
        print(i)
print(pereborg.__name__)

