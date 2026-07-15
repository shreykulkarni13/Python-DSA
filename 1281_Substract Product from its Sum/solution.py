n = 234

def subtractProductAndSum(n):
    sum = 0
    product = 1

    a = str(n)
    for i in range (0,len(a)):
        sum = sum + int(a[i])
        product = product*int(a[i])

    return product - sum

print(subtractProductAndSum(n))
    