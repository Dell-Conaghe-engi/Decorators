from main import check_time


@check_time
def pereborg():
    nums = range(1, 10000000)
    for i in nums:
        i = i ** 2
        print(i)


print(pereborg())
