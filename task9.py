def multiples(mul1, mul2):
    nums = 0
    for num in range(1000):
        if num % mul1 == 0 or num % mul2 == 0:
            nums += num
    print(nums)

multiples(3, 5)