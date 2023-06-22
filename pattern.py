def print_pattern(number):
    flag = 1
    while flag <= number:
        result =''
        for i in range(1,flag+1):
            result += str(i)
        print(result)
        flag +=1