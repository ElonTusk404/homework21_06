def find_prime_factors(number):
    result = []
    delitel = 2
    while delitel <= number:
        if number % delitel == 0:
            result.append(delitel)
            number = number // 2
        else:
            delitel +=1
    return result
test = find_prime_factors(99)
print(test)